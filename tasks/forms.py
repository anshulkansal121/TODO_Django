from pyexpat import model
from tkinter import Widget
from turtle import title
from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add New Task...'}))
    class Meta:
        model=task
        fields='__all__'