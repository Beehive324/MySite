#django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import User


class FormRegistration(UserCreationForm): # Form Registration Class to create an user
    email = forms.EmailField(max_length=60, help_text='Required.Add a valid email address')

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")


 
class UserAuthenticationForm(forms.ModelForm): # UserAuthenticationForm

    password = forms.CharField(label='Password', widget=forms.PasswordInput) #sets password witht the following values

    class Meta:  # introduces a class Meta
        model = User
        fields = ('password', 'email')

    def clean(self): # clean function taking the paramater self
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")



class UserUpdateForm(forms.ModelForm): # Function to Update the User form

    class Meta: # Meta class
        model = User
        fields = ('email', 'username') # Contains fields

    def clean_email(self): # clean_email function takes the parameter as self
        if self.is_valid():
            email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is in use.' % user)


    def clean_username(self): #  function for clean_username takes self as a parameter
        if self.is_valid():
            username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is in use.' % user)



class ContactForm(forms.Form): # Defines a contact form
    name = forms.CharField(required=True) # following parameters for the ContactForm
    subject = forms.CharField(required=True)
    email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    message = forms.CharField(widget=forms.Textarea(attrs={'class':'.form-signin'}), required=True)


