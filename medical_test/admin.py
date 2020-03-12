from django.contrib import admin

from .models import Measurement, Age, MedicalProcedure
from .models import Parameter, MedicalProcedureResult
from .models import ParameterValue


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MedicalProcedure)
class MedicalProcedureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'female',
        'male'
    )


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement',
        'medical_procedure'
    )


@admin.register(MedicalProcedureResult)
class MedicalProcedureResultAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'medical_procedure',
        'result'
    )


@admin.register(ParameterValue)
class ParameterValueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'parameter'
    )
