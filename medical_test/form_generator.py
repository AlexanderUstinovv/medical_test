from django.forms import Form

from .models import MedicalProcedure, Parameter
from .forms import FormFieldDescription, INTEGER_FIELD, get_form


def create_param_description(parameter: Parameter
                             ) -> FormFieldDescription:
    description = FormFieldDescription(
        id=parameter.id,
        label=parameter.name,
        measurement=parameter.measurement.name,
        field_type=INTEGER_FIELD
    )

    return description


def generate_form_by_recommendation(
        medical_procedure: MedicalProcedure) -> Form:
    parameters = Parameter.objects.filter(
        medical_procedure=medical_procedure)
    descriptions = map(lambda param: create_param_description(param),
                       parameters)
    return get_form(list(descriptions))
