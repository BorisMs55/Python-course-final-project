from django.contrib import admin
from .models import Employee, Department, Job


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Job)
