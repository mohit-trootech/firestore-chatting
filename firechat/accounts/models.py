# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from firechat.utils.constants import ModelMediaUrl


def _upload_to(self):
    return ModelMediaUrl.USER.value.format(id=self.id)


class User(AbstractUser):
    profile = models.ImageField(upload_to=_upload_to, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)

    def __str__(self):
        return self.username
