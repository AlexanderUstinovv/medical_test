from typing import List

from collections import namedtuple

import django.forms as forms

from django.forms.fields import Field

FLOAT_FILED = 'float_field'
STRING_FIELD = 'string_field'
INTEGER_FIELD = 'integer_field'

field_generators = {
    INTEGER_FIELD: lambda label, help_text: forms.IntegerField(
        label=label, help_text=help_text),
    STRING_FIELD: lambda label, help_text: forms.CharField(
        label=label, help_text=help_text),
    FLOAT_FILED: lambda label, help_text: forms.FloatField(
        label=label, help_text=help_text)
}

FormFieldDescription = namedtuple(
    'FormFieldDescription', ['field_type', 'label',
                             'measurement', 'id']
)


class MedicalTestBaseForm(forms.Form):
    pass


def get_field(field_description: FormFieldDescription) -> Field:
    field_function = field_generators.get(field_description.field_type)
    return field_function(field_description.label,
                          field_description.measurement)


def get_form(descriptions: List[FormFieldDescription]) -> forms.Form:
    form = MedicalTestBaseForm()

    # TODO: add validation
    for item in descriptions:
        form.fields[item.id] = get_field(item)
    return form
