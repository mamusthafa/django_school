from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Expense
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max, Min, Sum
from .forms import ExpenseForm
#from .filters import OrderFilter



@login_required
def expense_create(request):
    if request.method == 'POST':
        expense = Expense(author=request.user)  
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('expense-list')
    else:
        form = ExpenseForm()
    return render(request, 'expense/expense_form.html', {'form': form})



def expense_list(request):
    expenses = Expense.objects.all().order_by('-date_posted')
    expensesum = Expense.objects.all().aggregate(Sum('amount'))
    # pagination code for function based views starts here
    page = request.GET.get('page', 1)
    paginator = Paginator(expenses, 5)

    try:
        expenses = paginator.page(page)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)
    # Pagination ends here
    context = {'expenses': expenses, 'expensesum': expensesum}
    return render(request, 'expense/expense_lists.html', context)

    
def expense_detail(request, id):
    expense = Expense.objects.get(id=id)
    return render(request, 'expense/expense_detail.html', {'expense': expense})


@login_required
def expense_update(request, id):
    expense = get_object_or_404(Expense, id=id)
    form = ExpenseForm(request.POST or None, request.FILES or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('/expense/expense_list')
    context = {"form": form}
    return render(request, 'expense/expense_update.html', context)


@login_required
def expense_delete(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('/expense/expense_list')
    context = {"expense": expense}
    return render(request, 'expense/expense_confirm_delete.html', context)
