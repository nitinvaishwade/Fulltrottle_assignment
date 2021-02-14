from django import forms
from .models import Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False





class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username': 'Username', 'email': 'Email', 'password': 'Password'}


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         labels = {'username': 'Username', 'email': 'Email', 'password': 'Password'}