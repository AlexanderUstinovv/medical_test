from django.contrib.auth.models import User

from .models import Parameter, ParameterValue
from .models import MedicalProcedure, MedicalProcedureResult


def create_param_value(parameter: Parameter,
                       medical_procedure_result: MedicalProcedureResult,
                       value: int) -> ParameterValue:
    return ParameterValue.objects.create(
        value=value,
        parameter=parameter,
        medical_procedure_result=medical_procedure_result
    )


def create_procedure_result(medical_procedure: MedicalProcedure,
                            user: User,
                            result: bool) -> MedicalProcedureResult:
    return MedicalProcedureResult.objects.create(
        user=user,
        result=result,
        # TODO: delete this parameter from model
        value=0,
        medical_procedure=medical_procedure
    )


def create_new_parameters(user: User,
                          medical_procedure: MedicalProcedure,
                          post_dict: dict) -> None:
    medical_procedure_result = create_procedure_result(
        medical_procedure,
        user,
        True
    )

    for key, value in post_dict:
        parameter = Parameter.objects.get(id=key)
        create_param_value(
            parameter,
            medical_procedure_result,
            value=value
        )
        max_border = parameter.maximum_border
        min_border = parameter.minimum_border
        if not min_border < value < max_border:
            medical_procedure_result.result = False
            medical_procedure_result.save()


def update_parameter(medical_procedure_result: MedicalProcedureResult,
                     post_dict: dict) -> None:
    for key, value in post_dict:
        parameter = ParameterValue.objects.filter(id=key)
        if parameter.exists():
            parameter.update(value=value)
            max_border = parameter.first().maximum_border
            min_border = parameter.first().minimum_border
            if not min_border < value < max_border:
                medical_procedure_result.result = False
                medical_procedure_result.save()


def handle_parameter_form(user: User,
                          medical_procedure_id: int,
                          post_dict: dict) -> None:
    medical_procedure = MedicalProcedure.objects.get(
        id=medical_procedure_id
    )

    medical_procedure_result = MedicalProcedureResult.objects.filter(
        user=user,
        medical_procedure=medical_procedure
    )

    if medical_procedure_result.exists():
        update_parameter(medical_procedure_result.first(), post_dict)
    else:
        create_new_parameters(user, medical_procedure, post_dict)
