#-*- coding: utf-8 -*-

from django.db import models

class Invite(models.Model):
    
    id = models.AutoField(primary_key=True, db_column="invite_id")   
    user = models.ForeignKey("users.Users",related_name='invite_user',null=False, blank=False)
    friend = models.ForeignKey("users.Users",related_name='invite_friend',db_column="friend_id", null=False, blank=False)
    date = models.DateTimeField(db_column="invite_dt")
    
    class Meta:
        db_table = "invite"
    
    def __unicode__(self):
        return self.nome
    
    
class InviteEmail(models.Model):
  
    id = models.AutoField(primary_key=True, db_column="invite_email_id")   
    user = models.ForeignKey("users.Users",null=False, blank=False)
    code = models.CharField(db_column="code_txt", max_length=32,null=False, blank=False)
    date = models.DateTimeField(db_column="invite_dt")
    
    class Meta:
        db_table = "invite_email"
    
    def __unicode__(self):
        return self.nome