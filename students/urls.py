from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView, UserStudentListView, SchoolCreateView, SchoolListView, SchoolDetailView, SchoolUpdateView, SchoolDeleteView
from . import views

urlpatterns = [
    path('', StudentListView.as_view(), name='student-home'),
    path('school_create/', SchoolCreateView.as_view(), name='school-create'),
    path('schools/', SchoolListView.as_view(), name='schools'),
    path('school_detail/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('school/<int:pk>/update/', SchoolUpdateView.as_view(), name='school-update'),
    path('school/<int:pk>/delete/', SchoolDeleteView.as_view(), name='school-delete'),
    path('user/<str:username>', UserStudentListView.as_view(), name='user-students'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('books/', views.book_list, name='book_list'),
    path('books/book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/update/', views.book_update, name='book-update'),
    path('books/<int:id>/delete/', views.book_delete, name='book-delete'),
    path('books/upload/', views.upload_book, name='upload_book'),

]