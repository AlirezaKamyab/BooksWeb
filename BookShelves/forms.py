from .models import Book
from django import forms
class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['BookName','Author','Rating', 'Pages', 'Checked', 'user']