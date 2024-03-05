from django import forms


class LoginForm(forms.Form):
    FullName=forms.CharField(max_length=50 , required=True , label="نام و نام خانوادگی")
    Email=forms.CharField(max_length=50 , required=True , widget=forms.EmailInput  , label="ایمیل")
    Password=forms.CharField(max_length=50 , required=True , widget=forms.PasswordInput , label="رمز ورود")