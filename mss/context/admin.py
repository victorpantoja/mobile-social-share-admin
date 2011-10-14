#-*- coding: utf-8 -*-

from django.contrib import admin
from context.models import Context

class ContextAdmin(admin.ModelAdmin):
    pass

admin.site.register(Context, ContextAdmin)