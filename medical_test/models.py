from django.contrib.auth.models import User
from django.db import models


class Measurement(models.Model):
    class Meta:
        db_table = 'measurement'

    name = models.CharField(max_length=6, verbose_name='Единицы измерения')
    description = models.TextField(verbose_name='Описание')


class Age(models.Model):
    class Meta:
        db_table = 'age'

    value = models.IntegerField(default=21, verbose_name='Возраст')


class MedicalProcedure(models.Model):
    class Meta:
        db_table = 'medical_procedure'

    # TODO: find the max length of this field
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    female = models.BooleanField(verbose_name='Для женщин', default=True)
    male = models.BooleanField(verbose_name='Для мужчин', default=True)
    age = models.ManyToManyField(Age, verbose_name='Возраст')


class Parameter(models.Model):
    class Meta:
        db_table = 'value'

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    measurement = models.OneToOneField(Measurement,
                                       verbose_name='Единицы измерения',
                                       on_delete=models.CASCADE)
    medical_procedure = models.OneToOneField(MedicalProcedure,
                                             verbose_name='Мед. процедура',
                                             on_delete=models.CASCADE)
    maximum_border = models.IntegerField(verbose_name='Верхняя граница', default=0)
    minimum_border = models.IntegerField(verbose_name='Нижняя граница', default=0)


class MedicalProcedureResult(models.Model):
    class Meta:
        db_table = 'medical_procedure_result'

    medical_procedure = models.OneToOneField(MedicalProcedure,
                                             verbose_name='Процедура',
                                             on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Значение')
    user = models.OneToOneField(User,
                                verbose_name='Пользователь',
                                on_delete=models.CASCADE)
    result = models.BooleanField(default=False, verbose_name='Значение в норме')


class ParameterValue(models.Model):
    class Meta:
        db_table = 'parameter_value'

    medical_procedure_result = models.OneToOneField(MedicalProcedureResult,
                                                    verbose_name='Результат процедуры',
                                                    on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Значение')
    parameter = models.OneToOneField(Parameter,
                                     verbose_name='Название параметра',
                                     on_delete=models.CASCADE)
