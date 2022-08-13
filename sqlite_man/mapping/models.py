from django.db import models


class Mapping(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    class Meta:
        unique_together = ['name', 'key']
