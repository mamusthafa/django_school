from django.urls import path
from . import views


urlpatterns = [
    path('expense_create/', views.expense_create, name='expense-create'),
    path('expense_list/', views.expense_list, name='expense-list'),
    path('expense_detail/<int:id>/', views.expense_detail, name='expense-detail'),
    path('<int:id>/update/', views.expense_update, name='expense-update'),
    path('expense/<int:id>/delete/', views.expense_delete, name='expense-delete'),
]