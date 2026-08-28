from django import forms
from .models import MoodEntry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = [
            "score",
            "reason",
            "tag",
            "energy_level"
            ]
  
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]    
