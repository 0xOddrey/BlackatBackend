from django.db import models
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import datetime
datetime.date.today()

class WtfWord(models.Model):
    name = models.CharField(max_length=150,
                              blank=True,
                              null=True)
    definition = models.CharField(max_length=750,
                              blank=True,
                              null=True)

    def __str__(self):
        return "%s" % (self.name)