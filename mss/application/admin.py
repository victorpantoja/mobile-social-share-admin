#-*- coding: utf-8 -*-

from django.contrib import admin
from application.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name','icon', 'token', 'callback_url')

admin.site.register(Application, ApplicationAdmin)