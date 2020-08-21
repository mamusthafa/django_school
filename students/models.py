from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Student(models.Model):
    firstname = models.CharField(max_length=150)
    fathername = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=13)
    present_class = models.CharField(max_length=100)
    address = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=50,default='00000')
    pdf = models.FileField(upload_to='pdfs', blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='student_photos')


    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('student-detail',kwargs={'pk':self.pk})



class School(models.Model):
    school_name = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=13)
    address = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    school_manual = models.FileField(upload_to='school_manual', null=True,blank=True)


    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        return reverse('school-detail',kwargs={'pk':self.pk}) 


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    pdf = models.FileField(upload_to='books/pdfs/', null=True, blank=True)
    cover = models.ImageField(upload_to = 'books/cover/', null=True, blank=True)

    def __str__(self):
        return self.title


class Faculty(models.Model):
    fac_fname = models.CharField(max_length=150)
    fac_lname = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=13)
    department = models.CharField(max_length=100)
    address = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    faculty_id = models.CharField(max_length=50,default='00000')
    image = models.ImageField(default='default.jpg', upload_to='faculty_photos',blank=True, null=True)


    def __str__(self):
        return self.fac_fname

    def get_absolute_url(self):
        return reverse('faculty_detail',kwargs={'pk':self.pk})

