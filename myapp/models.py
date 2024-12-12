from django.db import models

# Create your models here.
class LoginTable(models.Model):
username  = models.charField(maxlength=30,blank=True,NUll=True)
password = models.charField(maxlength=30,blank=True,NUll=True)
usertype = models.charField(maxlength=30,blank=True,NUll=True)

class usertable(models.Model):
Name = models.charField(maxlength=30,blank=True,NUll=True)
phone number = models.BigIntegerField(maxlength=30,blank=True,Null=True)
loginid = models.ForeignKey(LoginTable,models.CASCADE,blank=True,null=True)



class FileTable(models.Model):
    file=models.FileField(blank=True,null=True)
    userid=loginid = models.ForeignKey(LoginTable,models.CASCADE,blank=True,null=True)
