from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .models import School
from .models import Book
from .forms import SchoolForm
from .forms import BookForm
from django.core.files.storage import FileSystemStorage


class StudentListView(ListView):
    model = Student
    template_name = 'students/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    ordering = ['firstname']
    paginate_by = 5


class UserStudentListView(ListView):
    model = Student
    template_name = 'students/user_students.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Student.objects.filter(author=user).order_by('-date_posted')


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['firstname','fathername','admission_no','present_class','mobile_no','address','pdf','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = ['firstname','fathername','admission_no','present_class','mobile_no','address','pdf','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.author:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    success_url = '/students'

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.author:
            return True
        return False




class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    fields = ['school_name','phone_no','address','school_manual']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'students/schools.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'schools'
    ordering = ['school_name']
    paginate_by = 5


""" class UserSchoolListView(ListView):
    model = School
    template_name = 'students/user_schools.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'schools'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return School.objects.filter(author=user).order_by('-date_posted') """


class SchoolDetailView(DetailView):
    model = School


class SchoolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = School
    fields = ['school_name','phone_no','address','school_manual']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        school = self.get_object()
        if self.request.user == school.author:
            return True
        return False


class SchoolDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = School
    success_url = 'students/schools'

    def test_func(self):
        school = self.get_object()
        if self.request.user == school.author:
            return True
        return False

#Books Module starts here
def book_list(request):
    books = Book.objects.all()
    return render(request, 'students/booklist.html', {'books':books})


@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'students/upload_books.html', {'form':form})


def book_detail(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'students/book_detail.html', {'book':book})


def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None,request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/students/books')
    context = {"form": form}
    return render(request, 'students/book_update.html', context)



def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/students/books')
    context = {"book": book}
    return render(request, 'students/book_confirm_delete.html', context)