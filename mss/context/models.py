#-*- coding: utf-8 -*-

from django.db import models
from application.models import Application
from django.contrib.auth.models import User


class Context(models.Model):

    id = models.AutoField(primary_key=True, db_column="context_id")
    user = models.ForeignKey(User, null=False, blank=False)
    context_type = models.ForeignKey("ContextType", null=False, blank=False)
    context = models.CharField(db_column="context_txt", max_length=400, null=False, blank=False)
    application = models.ManyToManyField(Application)
    updated = models.DateTimeField(db_column="update_dt")

    class Meta:
        db_table = "context"

    def __unicode__(self):
        return self.user.username


class ContextType(models.Model):

    id = models.AutoField(primary_key=True, db_column="context_type_id")
    description = models.CharField(db_column="description_txt", max_length=20, null=False, blank=False)

    class Meta:
        db_table = "context_type"

    def __unicode__(self):
        return self.description
