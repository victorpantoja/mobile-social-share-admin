#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    gender = models.CharField(db_column="gender_flg", max_length=1, null=False, blank=False)
    tokens = models.CharField(db_column="tokens_txt", max_length=400, null=True, blank=True)

    class Meta:
        db_table = "user_profile"
