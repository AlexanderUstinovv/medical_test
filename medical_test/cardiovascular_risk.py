from collections import namedtuple

from .models import CardiovascularScore

PersonalData = namedtuple('PersonalData', ['smoking',
                                           'sex',
                                           'cholesterol',
                                           'age',
                                           'systolic_pressure'])

RISK_MIN_BORDER = 35


def calculate_risk(person_data: PersonalData) -> bool:
    if person_data.age < RISK_MIN_BORDER:
        return False

    scores = CardiovascularScore.objects.filter(
        smoking=person_data.smoking,
        sex=person_data.sex,
        cholesterol_min__lw=person_data.cholesterol,
        cholesterol_max__gt=person_data.cholesterol,
        age_min__lw=person_data.age,
        age_min__gt=person_data.age,
        systolic_pressure_min__lw=person_data.systolic_pressure,
        systolic_pressure_min__gt=person_data.systolic_pressure
    )

    if scores.exist():
        if len(scores) == 1:
            return scores.first().high_risk
        elif len(scores) > 1:
            scores.filter(high_risk=True)
            if scores.exists():
                return True
            else:
                return False
        return False
    return False
