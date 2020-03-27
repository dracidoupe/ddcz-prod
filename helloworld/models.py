from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ZldMain(models.Model):
    rocnik = models.CharField(unique=True, max_length=6)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'zld_main'
