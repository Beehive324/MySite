from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from user.forms import FormRegistration, UserAuthenticationForm, UserUpdateForm, ContactForm


def reg_view(request):  #registration view                            
    context = {}
    if request.POST:
        form = FormRegistration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email =email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = FormRegistration()
        context['registration_form'] = form
    return render(request, 'user/register.html', context) #links to the html file
        
def logout_view(request): # this is the logout view
    logout(request) # refreshes the page in order to logout
    return redirect('home')  # redirects to home



def login_view(request): # this is the login view

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST: # if its a post request
        form = UserAuthenticationForm(request.POST)
        if form.is_valid(): # if the form is valid
            email = request.POST['email'] # sets the value for the email
            password = request.POST['password'] # sets the value for the password
            user = authenticate(email=email, password=password) # sets the value for the password

            if user:
                login(request, username)
                return redirect("home")
    
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)



def user_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial ={
                      "email": request.POST['email'],
                      "username": request.POST['username'],
            }
            form.save()
            context["true_message"] = "Sucessful"
    else:
        form = UserUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'user/user.html', context)
    

def contact_view(request):
    if request.method == "GET":
         form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = name + ':\n' + form.cleaned_data['message']
            try:
                send_mail(subject, message, email,['myemail@mydomain.com'])
            except BadHeaderError:
                messages.add_message(request,messages.ERROR, 'Message Not Sent')
                return HttpResponse("Invalid header found.")

                messages.add_message(request, messages.SUCCESS, 'Message has been Sent')
                return redirect(reverse('home'))
            else:
                messages.add_message(request,messages.ERROR, 'Invalid Form Data;Message has not been sent')
    return render(request, 'user/contact.html', {"form":form})








































