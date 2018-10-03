from django.db import models

class Employee(models.Model):
	name = models.TextField()
	age = models.IntegerField()
	email = models.EmailField()
	title = models.CharField(max_length=50)
	salary = models.FloatField()
	headquarter = models.CharField(max_length=30)
	status = models.BooleanField()

	def __str__(self):
		return self.name