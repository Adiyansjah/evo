from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    identifier = forms.CharField(max_length=100)
    address = forms.CharField(required=False)
    country = forms.CharField(max_length=50)
    province = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)