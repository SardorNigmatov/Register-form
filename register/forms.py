from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'user_surname', 'phone_number', 'email', 'company', 'gender']
