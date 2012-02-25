#-*- coding: utf-8 -*-

from django.db import models


class Application(models.Model):

    id = models.AutoField(primary_key=True, db_column="application_id")
    name = models.CharField(db_column="name_txt", max_length=200, null=False, blank=False)
    icon = models.CharField(db_column="icon_txt", max_length=200, null=True, blank=True)
    token = models.CharField(db_column="token_txt", max_length=32, null=False, blank=False)
    callback_url = models.CharField(db_column="callback_url_txt", max_length=200, null=False, blank=False)

    class Meta:
        db_table = "application"

    def __unicode__(self):
        return self.name
