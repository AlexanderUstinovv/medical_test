from .models import MedicalProcedure, Age


def recommend_medical_test(sex: str, age: int):
    age = Age.objects.get(value=age)
    procedures = MedicalProcedure.objects.filter(sex=sex, age__in=[age.id])
    return procedures
