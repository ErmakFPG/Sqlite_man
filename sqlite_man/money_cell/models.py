from django.db import models
from user.models import User


class MoneyCell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
