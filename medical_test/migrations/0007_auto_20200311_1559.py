# Generated by Django 3.0.3 on 2020-03-11 15:59

from django.core.management import call_command
from django.db import migrations

PARAMETER_MODEL_NAME = 'Parameter'
APP_LABEL = 'medical_test'
FIXTURE_NAME = 'parameter.json'
LOAD_DATA_COMMAND = 'loaddata'


def load_parameters_from_fixture(apps, schema_editor):
    call_command(LOAD_DATA_COMMAND, FIXTURE_NAME)


def delete_parameters(apps, schema_editor):
    Parameter = apps.get_model(APP_LABEL, PARAMETER_MODEL_NAME)
    Parameter.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('medical_test', '0006_auto_20200311_1557'),
    ]

    operations = [
        migrations.RunPython(load_parameters_from_fixture, delete_parameters)
    ]
