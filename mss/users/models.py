#-*- coding: utf-8 -*-

from django.db import models

class Users(models.Model):
        
    id = models.AutoField(primary_key=True, db_column="user_id")
    username = models.CharField(db_column="username_txt", max_length=200,null=False, blank=False)
    lastname = models.CharField(db_column="lastname_txt", max_length=100,null=False, blank=False)
    firstname = models.CharField(db_column="firstname_txt", max_length=100,null=False, blank=False)
    gender = models.CharField(db_column="gender_flg", max_length=100,null=False, blank=False)
    password = models.CharField(db_column="password_txt", max_length=32,null=False, blank=False)
    created = models.DateTimeField(db_column="criate_dt")
    lastlogin = models.DateTimeField(db_column="lastlogin_dt")

    class Meta:
        db_table = "users"
    
    def __unicode__(self):
        return self.username
