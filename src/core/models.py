from django.db import models

# Create your models here.
class Discuss(models.Model):
	name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	phone = models.CharField(max_length=120, blank=True, null=True)
	description = models.TextField(blank=True, null=True)