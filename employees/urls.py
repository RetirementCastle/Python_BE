from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', views.EmployeeView)
router.register('users', views.UserView)


urlpatterns = [
	path('', include(router.urls))
]