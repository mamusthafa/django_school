from django.urls import path
from .views import ExpenseCreateView, ExpenseListView, ExpenseDetailView
from . import views


urlpatterns = [
    path('expense_create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expense_list/', ExpenseListView.as_view(), name='expense-list'),
    path('expense_detail/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expense_lists/', views.expense_list, name='expense-lists'),
]