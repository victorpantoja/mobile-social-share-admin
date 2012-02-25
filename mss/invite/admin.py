#-*- coding: utf-8 -*-

from django.contrib import admin
from invite.models import Invite, InviteEmail


class InviteAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'date',)


class InviteEmailAdmin(admin.ModelAdmin):
    list_display = ('user', 'date',)

admin.site.register(Invite, InviteAdmin)
admin.site.register(InviteEmail, InviteEmailAdmin)
