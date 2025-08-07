from django import forms
from .models import ToDoList

class ToDoList(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["first_name", "items"]
