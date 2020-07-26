from django.contrib import admin

from .models import Student
from .models import School

# Register your models here.
admin.site.register(Student)
admin.site.register(School)
