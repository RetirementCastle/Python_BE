from django.db import models
from datetime import date
from django_auth_ldap.backend import LDAPBackend

class Employee(models.Model):
	name = models.TextField()
	age = models.IntegerField()
	email = models.EmailField()
	username = models.CharField(max_length=15,default='0')
	password = models.TextField(default='0000000')
	identification = models.CharField(max_length=12, default='0')
	title = models.CharField(max_length=50)
	phone = models.CharField(max_length=10, default='0000000')
	salary = models.FloatField()
	headquarter = models.IntegerField()
	status = models.BooleanField()
	ip = models.CharField(max_length=15, default='0')
	token = models.TextField(default='0')
	operation = models.IntegerField(default=0)
	created_at = models.DateField(("Date"), default=date.today)
	last_login = models.DateField(("Date"), default=date.today)

	def __str__(self):
		return self.name


def authenticate_credentials(self, payload):
    try:
        username = payload.get('username')

        if username:
            user = User.objects.get(pk=username, is_active=True)
            user = LDAPBackend().authenticate(username, password)
        else:
            msg = 'Invalid payload'
            raise exceptions.AuthenticationFailed(msg)
    except User.DoesNotExist:
        msg = 'Invalid signature'
        raise exceptions.AuthenticationFailed(msg)

    return user



class User(models.Model):
	nursinghome = models.IntegerField()
	username = models.CharField(max_length=15,default='0')
	password = models.TextField(default='0000000')
	token = models.TextField(default='0')