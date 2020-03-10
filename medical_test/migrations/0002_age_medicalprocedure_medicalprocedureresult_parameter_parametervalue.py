# Generated by Django 3.0.3 on 2020-03-10 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=21, verbose_name='Возраст')),
            ],
            options={
                'db_table': 'age',
            },
        ),
        migrations.CreateModel(
            name='MedicalProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('female', models.BooleanField(default=True, verbose_name='Для женщин')),
                ('male', models.BooleanField(default=True, verbose_name='Для мужчин')),
                ('age', models.ManyToManyField(to='medical_test.Age', verbose_name='Возраст')),
            ],
            options={
                'db_table': 'medical_procedure',
            },
        ),
        migrations.CreateModel(
            name='MedicalProcedureResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Значение')),
                ('result', models.BooleanField(default=False, verbose_name='Значение в норме')),
                ('medical_procedure', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_test.MedicalProcedure', verbose_name='Процедура')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'db_table': 'medical_procedure_result',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('maximum_border', models.IntegerField(default=0, verbose_name='Верхняя граница')),
                ('minimum_border', models.IntegerField(default=0, verbose_name='Нижняя граница')),
                ('measurement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_test.Measurement', verbose_name='Единицы измерения')),
                ('medical_procedure', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_test.MedicalProcedure', verbose_name='Мед. процедура')),
            ],
            options={
                'db_table': 'value',
            },
        ),
        migrations.CreateModel(
            name='ParameterValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Значение')),
                ('medical_procedure_result', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_test.MedicalProcedureResult', verbose_name='Результат процедуры')),
                ('parameter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_test.Parameter', verbose_name='Название параметра')),
            ],
            options={
                'db_table': 'parameter_value',
            },
        ),
    ]