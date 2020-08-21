from django.contrib import admin

from .models import Student
from .models import School
from .models import Book
from .models import Faculty

# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Book)
admin.site.register(Faculty)
