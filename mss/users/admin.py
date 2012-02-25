#-*- coding: utf-8 -*-

from django.contrib import admin
from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender',)

admin.site.register(UserProfile, UserProfileAdmin)
