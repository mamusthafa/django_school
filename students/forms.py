from django import forms
from .models import School
from .models import Book
from .models import Faculty

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','phone_no','address']

#BookForm starts here
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','pdf','cover']


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['fac_fname','fac_lname','mobile_no','department','address','faculty_id','image']

