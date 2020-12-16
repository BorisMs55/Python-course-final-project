from rest_framework import serializers
from . import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary', 'commission_pct',
                  'manager', 'photo', 'job', 'department')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('name',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('name',)
