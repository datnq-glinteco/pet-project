from django.db import models
from constants import Choice


class Test(models.Model):
    shirt_size = models.CharField(choices=Choice.SIZE, max_length=1)