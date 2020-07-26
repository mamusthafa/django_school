from django import forms
from .models import School
from .models import Book

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','phone_no','address']

#BookForm starts here
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','pdf','cover']

