from django import forms
from django.contrib.auth.models import User

from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}) , required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}) , required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}) , required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        passw = cleaned_data.get('password')
        c_pass = cleaned_data.get('confirm_password')

        if c_pass != passw:
            self.add_error('confirm_password', "Password didn't matched")
        return cleaned_data

class ProfileCreationForm(forms.ModelForm):

    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone'}), max_length=15, required=False)
    profession = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Profession'}), max_length=50, required=False)
    address = forms.TimeField(widget=forms.TextInput(attrs={'placeholder':'Address here...'}) , required=False)
    facebook = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Facebook Link'}), required=False)
    instagram = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Instagram Link'}), required=False)
    linkedin = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Linkedin Link'}), required=False)
    class Meta:
        model = Profile
        fields = (
                "phone",
                "profession",
                "address",
                "facebook",
                "instagram",
                "linkedin"
            )
