from django.contrib.auth.models import User
from django.db import models


class Measurement(models.Model):
    class Meta:
        db_table = 'measurement'
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    name = models.CharField(max_length=10, verbose_name='Единицы измерения')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Age(models.Model):
    class Meta:
        db_table = 'age'
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возрасты'

    value = models.IntegerField(default=21, verbose_name='Возраст')

    def __str__(self):
        return str(self.value)


class MedicalProcedure(models.Model):
    class Meta:
        db_table = 'medical_procedure'
        verbose_name = 'Медицинская процедура'
        verbose_name_plural = 'Медицинские процедуры'

    # TODO: find the max length of this field
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    female = models.BooleanField(verbose_name='Для женщин', default=True)
    male = models.BooleanField(verbose_name='Для мужчин', default=True)
    age = models.ManyToManyField(Age, verbose_name='Возраст')

    def __str__(self):
        return self.name


class Parameter(models.Model):
    class Meta:
        db_table = 'value'
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    measurement = models.ForeignKey(Measurement,
                                    verbose_name='Единицы измерения',
                                    on_delete=models.CASCADE)
    medical_procedure = models.ForeignKey(MedicalProcedure,
                                          verbose_name='Мед. процедура',
                                          on_delete=models.CASCADE)
    female_maximum_border = models.DecimalField(max_digits=7, decimal_places=2,
                                                verbose_name='Верхняя граница женщины', default=0)
    female_minimum_border = models.DecimalField(max_digits=7, decimal_places=2,
                                                verbose_name='Нижняя граница женщины', default=0)
    male_maximum_border = models.DecimalField(max_digits=7, decimal_places=2,
                                              verbose_name='Врехняя граница мужчины', default=0)
    male_minimum_border = models.DecimalField(max_digits=7, decimal_places=2,
                                              verbose_name='Нижняя граница мужчины', default=0)

    def __str__(self):
        return self.name


class MedicalProcedureResult(models.Model):
    class Meta:
        db_table = 'medical_procedure_result'
        verbose_name = 'Результат мед. процедуры'
        verbose_name_plural = 'Результаты мед. процедур'

    medical_procedure = models.ForeignKey(MedicalProcedure,
                                          verbose_name='Процедура',
                                          on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Значение')
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    result = models.BooleanField(default=False, verbose_name='Значение в норме')

    def __str__(self):
        return self.medical_procedure.name


class ParameterValue(models.Model):
    class Meta:
        db_table = 'parameter_value'
        verbose_name = 'Результат параметра'
        verbose_name_plural = 'Результаты параметров'

    medical_procedure_result = models.ForeignKey(MedicalProcedureResult,
                                                 verbose_name='Результат процедуры',
                                                 on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2,
                                verbose_name='Значение', default=0)
    parameter = models.ForeignKey(Parameter,
                                  verbose_name='Название параметра',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.parameter.name


class CardiovascularScore(models.Model):
    class Meta:
        db_table = 'cardiovascular_score'
        verbose_name = 'Шкала Score сердечно-сосудистого риска'
        verbose_name_plural = 'Шкалы Score сердечно-сосудистого риска'

    MALE = 'M'
    FEMALE = 'F'
    SEX_TYPES = (
        (MALE, 'Муж.'),
        (FEMALE, 'Жен.'),
    )

    sex = models.CharField(max_length=6, choices=SEX_TYPES, verbose_name='Пол')
    smoking = models.BooleanField(default=False, verbose_name='Курящий')
    cholesterol_min = models.DecimalField(max_digits=6, decimal_places=2,
                                          verbose_name='Уровень холестирина нижняя граница',
                                          default=0)
    cholesterol_max = models.DecimalField(max_digits=6, decimal_places=2,
                                          verbose_name='Уровень холестирина верхняя граница',
                                          default=0)
    systolic_pressure_max = models.DecimalField(max_digits=6, decimal_places=2,
                                                verbose_name='Систолическое давление верхняя граница',
                                                default=0)
    systolic_pressure_min = models.DecimalField(max_digits=6, decimal_places=2,
                                                verbose_name='Систолическое давление нижняя граница',
                                                default=0)
    age_min = models.IntegerField(verbose_name='Возраст нижняя граница')
    age_max = models.IntegerField(verbose_name='Возраст верхняя граница')
    result = models.IntegerField(verbose_name='Процент риска заболевания')
