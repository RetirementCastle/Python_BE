from rest_framework import serializers
from .models import Employee
from .models import User

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'name', 'age', 'title', 'email' ,'salary', 'headquarter', 'status', 'username', 'password',
		 'identification', 'phone','ip', 'token', 'operation','created_at', 'last_login')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'token', 'nursinghome')