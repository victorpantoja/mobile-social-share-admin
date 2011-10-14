#-*- coding: utf-8 -*-

from django.contrib import admin
from friendship.models import Friendship

class FriendShipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Friendship, FriendShipAdmin)