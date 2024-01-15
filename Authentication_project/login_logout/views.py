from django.shortcuts import render,redirect
from login_logout.forms import RegistrationForm
from django.contrib import messages 
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            messages.success( request, 'Account registered successfully.')
            form.save() 
            return redirect('login')
    else: 
        form = RegistrationForm() 
    return render(request, 'register.html',{'form':form,'type':'Register'})  

def Login(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request=request, data = request.POST)  
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password'] 
            user = authenticate(username = username, password = password) 
            if user is not None: 
                messages.success( request, 'Logged in successfully.')
                login(request,user) 
                return redirect('profile') 
            else: 
            # Display an error message using the messages framework.
             messages.success(request, 'Invalid username or password. Please try again.')
    else: 
        auth_form= AuthenticationForm() 
    return render(request, 'register.html',{'form': auth_form, 'type':'Login'}) 
@login_required
def change_pass(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, data = request.POST) 
        if pass_form.is_valid():
            messages.success( request, 'Updated password successfully.')
            pass_form.save()  
            update_session_auth_hash(request,pass_form.user) 
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user=request.user) 
    return render(request, 'change_pass.html',{'form':pass_form}) 

@login_required
def change_pass_without_oldPass(request):
    if request.method == 'POST': 
        form = SetPasswordForm(request.user, data= request.POST)
        if form.is_valid():
            messages.success( request, 'Updated password successfully.')
            form.save()  
            update_session_auth_hash(request,form.user) 
            return redirect('profile') 
    else: 
        form = SetPasswordForm(user=request.user) 
    return render(request, 'change_pass.html',{'form':form})


def home(request):
    return render(request, 'home.html') 

@login_required
def profile(request):
    return render(request, 'profile.html') 

@login_required      
def Logout(request): 
    logout(request) 
    messages.success( request, 'Logged out successfully.')
    return redirect('homepage') 






