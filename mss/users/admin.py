#-*- coding: utf-8 -*-

from django.contrib import admin
from users.models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('lastname','firstname', 'username', 'gender', 'created', 'lastlogin')

admin.site.register(Users, UsersAdmin)