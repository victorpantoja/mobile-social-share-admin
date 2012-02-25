#-*- coding: utf-8 -*-

from django.db import models


class Status(models.Model):

    id = models.AutoField(primary_key=True, db_column="status_id")
    status = models.CharField(db_column="status_txt", max_length=400, null=False, blank=False)
    date = models.DateTimeField(db_column="created_dt")

    class Meta:
        db_table = "system"
        verbose_name_plural = "Status"

    def __unicode__(self):
        return self.status
