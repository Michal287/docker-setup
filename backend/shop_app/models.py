from django.db import models


class Opinion(models.Model):
    description = models.TextField(null=False)
