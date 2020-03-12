from .models import MedicalProcedure, Age

MALE = 'M'


def fetch_age(age_value: int):
    current_age = Age.objects.filter(value=age_value)
    age = Age.objects.all().first()
    if current_age.exists():
        age = current_age.first()
    else:
        ages = Age.objects.all()
        for item in ages:
            if item.value > age_value:
                age = item
                break
    return age


def recommend_medical_test(sex: str, age: int):
    age = fetch_age(age)

    if sex == MALE:
        return MedicalProcedure.objects.filter(male=True,
                                               age__in=[age.id])
    return MedicalProcedure.objects.filter(female=True,
                                           age__in=[age.id])
