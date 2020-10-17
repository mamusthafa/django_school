from django.shortcuts import render, get_object_or_404, redirect
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
from .forms import FacultyForm
from .models import Faculty
from .models import Post
from django.core.files.storage import FileSystemStorage
from .filters import OrderFilter


# Student Section Starts Here
class StudentListView(ListView):
    model = Student
    # template_name = 'students/home.html'  # <app>/<model>_<viewtype>.html  = students/student_list.html
    # context_object_name = 'students'      by default = object_list
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
    model = Student   # <app>/<model>_<viewtype>.html  = students/student_detail.html


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student    # <app>/<model>_form.html  = students/student_form.html
    fields = ['firstname', 'fathername', 'admission_no',
              'present_class', 'mobile_no', 'address', 'pdf', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student    # <app>/<model>_form.html  = students/student_form.html
    fields = ['firstname', 'fathername', 'admission_no',
              'present_class', 'mobile_no', 'address', 'pdf', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.author:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student     # <app>/<model>_confirm_delete.html
    success_url = '/students'

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.author:
            return True
        return False

# Student section ends here ##################################


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    fields = ['school_name', 'phone_no', 'address', 'school_manual']

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
    fields = ['school_name', 'phone_no', 'address', 'school_manual']

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

# Books Module starts here


def book_list(request):
    books = Book.objects.all()
    return render(request, 'students/booklist.html', {'books': books})


@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'students/upload_books.html', {'form': form})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'students/book_detail.html', {'book': book})


@login_required
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/students/books')
    context = {"form": form}
    return render(request, 'students/book_update.html', context)


@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/students/books')
    context = {"book": book}
    return render(request, 'students/book_confirm_delete.html', context)


# Faculty Module Starts here
@login_required
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fac_list')
    else:
        form = FacultyForm()
    return render(request, 'students/add_faculty.html', {'form': form})


def faculty_list(request):
    faculties = Faculty.objects.all()
    # filter and search codes starts here
    myFilter = OrderFilter(request.GET, faculties)
    faculties = myFilter.qs
    # filter and search codes ends here
    context = {'faculties': faculties, 'myFilter': myFilter}
    return render(request, 'students/faculty_list.html', context)


@login_required
def faculty_update(request, id):
    faculty = get_object_or_404(Faculty, id=id)
    form = FacultyForm(request.POST or None,
                       request.FILES or None, instance=faculty)
    if form.is_valid():
        form.save()
        return redirect('/students/faculty/faculty_list')
    context = {"form": form}
    return render(request, 'students/faculty_update.html', context)


def faculty_detail(request, id):
    faculty = Faculty.objects.get(id=id)
    return render(request, 'students/faculty_details.html', {'faculty': faculty})


# Post Section starts here
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post    # <app>/<model>_form.html  = students/post_form.html
    fields = ['title', 'description', 'featured_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post   # <app>/<model>_<viewtype>.html  = students/post_detail.html


class PostListView(ListView):
    model = Post  # <app>/<model>_<viewtype>.html  = students/post_detail.html
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    # <app>/<model>_form.html  = students/student_form.html
    fields = ['title', 'description', 'featured_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post     # <app>/<model>_confirm_delete.html
    success_url = '/students/post_list'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False







