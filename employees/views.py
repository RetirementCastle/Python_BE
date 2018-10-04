from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from .models import User
from .serializers import UserSerializer

class EmployeeView(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer