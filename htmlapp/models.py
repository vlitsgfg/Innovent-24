from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
class Students(models.Model):
    S_id = models.CharField(max_length=255,unique=True)
    S_name = models.CharField(max_length=255)
    S_branch=models.CharField(max_length=10,null=True)
    S_category=models.CharField(max_length=255)
    S_totalfee=models.IntegerField(null=True)
    S_buildingfee=models.IntegerField(null=True)
    S_paid=models.IntegerField(null=True)
    S_due=models.IntegerField(null=True)
    def __str__(self):
        return self.S_id
    class Meta:
        ordering = ['S_name']
class FilesUpload(models.Model):
    file=models.FileField()
