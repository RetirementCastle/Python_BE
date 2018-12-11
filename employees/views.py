from django.shortcuts import render
from rest_framework import viewsets
from django_auth_ldap.backend import LDAPBackend
from .models import Employee
from .serializers import EmployeeSerializer
from .models import User
from .serializers import UserSerializer


class EmployeeView(viewsets.ModelViewSet):
	queryset = Employee.objects.all() 
	#queryset = LDAPBackend().authenticate(username, password)
	serializer_class = EmployeeSerializer

	def authenticate_credentials(self, payload):
		try:
			user_id = payload.get('user_id')

			if user_id:
				user = User.objects.get(pk=user_id, is_active=True)
			else:
				msg = 'Invalid payload'
				raise exceptions.AuthenticationFailed(msg)
		except User.DoesNotExist:
			msg = 'Invalid signature'
			raise exceptions.AuthenticationFailed(msg)

		return user 


class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def votes(self, request, *args, **kwargs):
	    survey = self.get_object()
	    votes = survey.survey_votes.all()
	    serializer = SurveyVotesSerializer(votes)
	    return Response(serializer.data)
