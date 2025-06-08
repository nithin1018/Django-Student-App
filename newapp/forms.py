# forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'hobby', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'hobby': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hobby'}),
        }
