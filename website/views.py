from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from .models import Homepage

""" def home(request):
    return render(request, 'website/home.html')

 """
