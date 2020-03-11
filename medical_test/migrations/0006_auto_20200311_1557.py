# Generated by Django 3.0.3 on 2020-03-11 15:57

from django.core.management import call_command
from django.db import migrations

PROCEDURE_MODEL_NAME = 'MedicalProcedure'
APP_LABEL = 'medical_test'
FIXTURE_NAME = 'medical_procedure.json'
LOAD_DATA_COMMAND = 'loaddata'


def load_procedures_from_fixture(apps, schema_editor):
    call_command(LOAD_DATA_COMMAND, FIXTURE_NAME)


def delete_procedures(apps, schema_editor):
    MedicalProcedure = apps.get_model(APP_LABEL, PROCEDURE_MODEL_NAME)
    MedicalProcedure.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('medical_test', '0005_auto_20200311_1545'),
    ]

    operations = [
        migrations.RunPython(load_procedures_from_fixture, delete_procedures)
    ]
