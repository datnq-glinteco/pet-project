from django.db import models


class Attachment(models.Model):
    attachment = models.FileField(upload_to="")