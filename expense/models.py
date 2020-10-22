from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Expense(models.Model):
    title = models.CharField(max_length=250)
    amount = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('expense-list')
