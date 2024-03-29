# Generated by Django 3.0.3 on 2020-03-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_test', '0007_auto_20200311_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardiovascularScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Муж.'), ('F', 'Жен.')], max_length=6, verbose_name='Пол')),
                ('smoking', models.BooleanField(default=False, verbose_name='Курящий')),
                ('cholesterol_min', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Уровень холестирина нижняя граница')),
                ('cholesterol_max', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Уровень холестирина верхняя граница')),
                ('systolic_pressure_max', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Систолическое давление верхняя граница')),
                ('systolic_pressure_min', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Систолическое давление нижняя граница')),
                ('age_min', models.IntegerField(verbose_name='Возраст нижняя граница')),
                ('age_max', models.IntegerField(verbose_name='Возраст верхняя граница')),
                ('result', models.IntegerField(verbose_name='Процент риска заболевания')),
            ],
            options={
                'verbose_name': 'Шкала Score сердечно-сосудистого риска',
                'verbose_name_plural': 'Шкалы Score сердечно-сосудистого риска',
                'db_table': 'cardiovascular_score',
            },
        ),
        migrations.AlterModelOptions(
            name='age',
            options={'verbose_name': 'Возраст', 'verbose_name_plural': 'Возрасты'},
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='medicalprocedure',
            options={'verbose_name': 'Медицинская процедура', 'verbose_name_plural': 'Медицинские процедуры'},
        ),
        migrations.AlterModelOptions(
            name='medicalprocedureresult',
            options={'verbose_name': 'Результат мед. процедуры', 'verbose_name_plural': 'Результаты мед. процедур'},
        ),
        migrations.AlterModelOptions(
            name='parameter',
            options={'verbose_name': 'Параметр', 'verbose_name_plural': 'Параметры'},
        ),
        migrations.AlterModelOptions(
            name='parametervalue',
            options={'verbose_name': 'Результат параметра', 'verbose_name_plural': 'Результаты параметров'},
        ),
    ]
