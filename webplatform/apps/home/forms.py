#encoding:utf-8
from django import forms
from apps.courses.models import Course


class EnrollForm(forms.Form):
    
    course = forms.CharField(widget=forms.HiddenInput())