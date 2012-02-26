#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):

    id = models.AutoField(primary_key=True, db_column="friendship_id")
    user = models.ForeignKey(User, related_name='user_user', null=False, blank=False)
    friend = models.ForeignKey(User, related_name='friend_user', db_column="friend_id", null=False, blank=False)
    date = models.DateTimeField(db_column="created_dt")

    class Meta:
        db_table = "friendship"

    def __unicode__(self):
        return self.user.username
