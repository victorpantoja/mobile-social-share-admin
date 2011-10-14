#-*- coding: utf-8 -*-

from django.contrib import admin
from invite.models import Invite, InviteEmail

class InviteAdmin(admin.ModelAdmin):
    pass

class InviteEmailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invite, InviteAdmin)
admin.site.register(InviteEmail, InviteEmailAdmin)