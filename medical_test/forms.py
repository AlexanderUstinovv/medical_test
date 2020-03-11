from typing import List

from collections import namedtuple

import django.forms as forms

from django.forms.fields import Field

INTEGER_FIELD = 'integer_field'
STRING_FIELD = 'string_field'

field_generators = {
    INTEGER_FIELD: lambda label: forms.IntegerField(label=label),
    STRING_FIELD: lambda label: forms.CharField(label=label)
}

FormFieldDescription = namedtuple(
    'FormFieldDescription', ['field_type', 'label',
                             'measurement', 'name']
)


class MedicalTestBaseForm(forms.Form):
    pass


def get_field(field_description: FormFieldDescription) -> Field:
    field_function = field_generators.get(field_description.field_type)
    return field_function(field_description.label)


def get_form(descriptions: List[FormFieldDescription]) -> forms.Form:
    form = MedicalTestBaseForm()

    # TODO: add validation
    for item in descriptions:
        form.fields[item.name] = get_field(item)
    return form
