from .models import MedicalProcedure, Age

MALE = 'M'


def recommend_medical_test(sex: str, age: int):
    age = Age.objects.get(value=age)

    if sex == MALE:
        return MedicalProcedure.objects.filter(male=True,
                                               age__in=[age.id])
    return MedicalProcedure.objects.filter(female=True,
                                           age__in=[age.id])
