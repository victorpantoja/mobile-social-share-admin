#-*- coding: utf-8 -*-

from django.contrib import admin
from context.models import Context, ContextType


class ContextAdmin(admin.ModelAdmin):
    list_display = ('user', 'context_type', 'context', 'updated')


class ContextTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Context, ContextAdmin)
admin.site.register(ContextType, ContextTypeAdmin)