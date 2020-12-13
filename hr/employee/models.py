from djmoney.models.fields import MoneyField
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    hire_date = models.DateField()
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='ILS')
    commission_pct = models.DecimalField(max_digits=4, decimal_places=2)
    manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name+' '+self.last_name)
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
