from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.EmployeeListView.as_view()),
    path('<int:pk>/', views.EmployeeDetailView.as_view()),
]
