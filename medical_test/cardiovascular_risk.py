from collections import namedtuple

from .models import CardiovascularScore

PersonalData = namedtuple('PersonalData', ['smoking',
                                           'sex',
                                           'cholesterol',
                                           'age',
                                           'systolic_pressure'])

RISK_MIN_BORDER = 40


def calculate_risk(person_data: PersonalData) -> int:
    if person_data.age < RISK_MIN_BORDER:
        return 0

    scores = CardiovascularScore.objects.filter(
        smoking=person_data.smoking,
        sex=person_data.sex,
        cholesterol_min__lte=person_data.cholesterol,
        cholesterol_max__gt=person_data.cholesterol,
        age_min__lte=person_data.age,
        age_min__gt=person_data.age,
        systolic_pressure_min__lte=person_data.systolic_pressure,
        systolic_pressure_min__gt=person_data.systolic_pressure
    )

    if scores.exists():
        return scores.first().result
    return 0
