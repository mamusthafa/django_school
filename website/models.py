from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Homepage(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_image = models.ImageField(upload_to='pages', null=True,blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('website-home') 



