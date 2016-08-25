from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=50)
    pwd = forms.CharField(label = 'password', max_length=50, widget=forms.PasswordInput)
    name = forms.CharField(label = 'first name', max_length=100)
    sirname = forms.CharField(label = 'last name', max_length=100)
    email = forms.CharField(label = 'email', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=50)
    pwd = forms.CharField(label = 'password', max_length=50, widget=forms.PasswordInput)