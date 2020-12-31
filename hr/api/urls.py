from django.urls import path, include
from .views import EmployeeViewset
# from rest_framework import routers
# router = routers.DefaultRouter()
#
# router.register('Employees', views.EmployeeViewset)

urlpatterns = [
    path('', EmployeeViewset.as_view, name="display_json"),
]