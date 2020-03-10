from django.db import models


class Measurement(models.Model):
    class Meta:
        db_table = 'measurement'

    name = models.CharField(max_length=6, verbose_name='Единицы измерения')
    description = models.TextField(verbose_name='Описание')
