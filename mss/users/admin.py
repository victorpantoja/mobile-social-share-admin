#-*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls.defaults import patterns
from django.http import HttpResponse

from users.models import UserProfile
from django.utils import simplejson
from django.views.generic.base import TemplateView


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender',)

    class Media:
        css = {
            "all": ("users/admin/users.css",)
        }
        js = ("users/admin/users.js","users/admin/jquery.cookie.js")

    def get_urls(self):
        urls = super(UserProfileAdmin, self).get_urls()
        urls_local = patterns('',
            (r'^auth', TemplateView.as_view(template_name="auth.html")),
        )
        return urls_local + urls

    def get_auth_token(self, request):
        return HttpResponse(simplejson.dumps({}), 'application/json', status=200)

admin.site.register(UserProfile, UserProfileAdmin)
