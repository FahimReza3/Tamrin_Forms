from django import forms


class LoginForm(forms.Form):
    def __init__(self , *args , **kwargs):
        super(LoginForm ,self).__init__(*args , **kwargs)
        for item in LoginForm.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"
            item.field.widget.attrs["style"] = "text-align:center;"

    id=forms.IntegerField(widget=forms.HiddenInput , label="")
    FullName=forms.CharField(max_length=50 , required=True , label="نام و نام خانوادگی" ,)
    Email=forms.CharField(max_length=50 , required=True , widget=forms.EmailInput()  , label="ایمیل")
    Password=forms.CharField(max_length=50 , required=True , widget=forms.PasswordInput , label="رمز ورود")