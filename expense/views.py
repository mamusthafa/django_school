from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Expense
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max, Min, Sum
#from .filters import OrderFilter


# Post Section starts here
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense    # <app>/<model>_form.html  = students/post_form.html
    fields = ['title', 'amount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ExpenseListView(ListView):
    model = Expense  # <app>/<model>_<viewtype>.html  = students/post_detail.html
    expensesum = Expense.objects.all().aggregate(Sum('amount'))
    ordering = ['-date_posted']
    paginate_by = 5 


def expense_list(request):
    expenses = Expense.objects.all()
    # filter and search codes starts he
    expensesum = Expense.objects.all().aggregate(Sum('amount'))
    # filter and search codes ends here
    context = {'expenses': expenses, 'expensesum': expensesum}
    return render(request, 'expense/expense_lists.html', context)

    
class ExpenseDetailView(DetailView):
    model = Expense   # <app>/<model>_<viewtype>.html  = students/post_detail.html
