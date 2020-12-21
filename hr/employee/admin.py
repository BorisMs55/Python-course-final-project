from django.contrib import admin
from .models import Employee, Department, Job


# class EmployeeAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("first_name", "last_name")}
#     readonly_fields = ('slug',)


#admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Job)
