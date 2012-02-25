#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Invite(models.Model):

    id = models.AutoField(primary_key=True, db_column="invite_id")
    user = models.ForeignKey(User, related_name='invite_user', null=False, blank=False)
    friend = models.ForeignKey(User, related_name='invite_friend', db_column="friend_id", null=False, blank=False)
    date = models.DateTimeField(db_column="invite_dt")

    class Meta:
        db_table = "invite"

    def __unicode__(self):
        return self.user.username


class InviteEmail(models.Model):

    id = models.AutoField(primary_key=True, db_column="invite_email_id")
    user = models.ForeignKey(User, null=False, blank=False)
    code = models.CharField(db_column="code_txt", max_length=32, null=False, blank=False)
    date = models.DateTimeField(db_column="invite_dt")

    class Meta:
        db_table = "invite_email"
        verbose_name_plural = "Email Invites"

    def __unicode__(self):
        return self.user.username
