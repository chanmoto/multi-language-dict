from django.db import models
import json

class Dictionary(models.Model):
     word = models.CharField(max_length=50, null=True, blank=True)
     def1 = models.CharField(max_length=1000, null=True, blank=True)
     def2 = models.CharField(max_length=1000, null=True, blank=True)
     def3 = models.CharField(max_length=1000, null=True, blank=True)
     def4 = models.CharField(max_length=1000, null=True, blank=True)
     def5 = models.CharField(max_length=1000, null=True, blank=True)
     def6 = models.CharField(max_length=1000, null=True, blank=True)
     def7 = models.CharField(max_length=1000, null=True, blank=True)
     def8 = models.CharField(max_length=1000, null=True, blank=True)
     def9 = models.CharField(max_length=1000, null=True, blank=True)
     def10 = models.CharField(max_length=1000, null=True, blank=True)

     def __str__(self):
         return self.word 
