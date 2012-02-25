#-*- coding: utf-8 -*-

from django.contrib import admin
from system.models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'date',)

admin.site.register(Status, StatusAdmin)
