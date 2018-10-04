from rest_framework import serializers
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'nursinghome','token')