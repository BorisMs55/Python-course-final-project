from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from . import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets


# Create your views here.


class EmployeeListView(APIView):
    """Employee List"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee/employee_list.html'

    def get(self, request):
        queryset = models.Employee.objects.all()
        return Response({'employees': queryset})

class EmployeeDetailView(APIView):
    """Employee"""

    def get(self, request, pk):
        employee = models.Employee.objects.get(id=pk)
        serializer = serializers.EmployeeDetailSerializer(employee)
        return Response(serializer.data)

# class EmployeeViewset(viewsets.ModelViewSet):
#     queryset = models.Employee.objects.all()
#     serializer_class = serializers.EmployeeSerializer


class JobViewset(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer


class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
