from rest_framework import serializers
from hr.employee import models


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('first_name', 'last_name', 'job')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('first_name', 'last_name', 'job')

class EmployeeDetailSerializer(serializers.ModelSerializer):

    manager = serializers.StringRelatedField(read_only=True)
    job = serializers.SlugRelatedField(slug_field="name", read_only=True)
    department = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = models.Employee
        exclude = ("commission_pct",)
        # fields = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary', 'commission_pct',
        #           'manager', 'photo', 'job', 'department')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('name',)
