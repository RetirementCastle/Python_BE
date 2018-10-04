from django.db import models
from datetime import date

class User(models.Model):
	nursinghome = models.IntegerField()
	username = models.CharField(max_length=15,default='0')
	password = models.TextField(default='0000000')
	token = models.TextField(default='0')

	def __str__(self):
		return self.username