from django import forms
from .models import NBook

class NBookForm(forms.ModelForm):
    class Meta:
        model = NBook
        fields = ['title', 'price', 'quantity', 'pubdate', 'publisher', 'authors']
        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = NBook
        fields = ['title', 'price', 'quantity', 'pubdate', 'publisher', 'authors']
        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-select'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }