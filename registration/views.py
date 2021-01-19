from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def Registration(request):
    if request.method == "POST":
        userform = RegistrationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('login')
    else:
        userform = RegistrationForm()
    return render(request, 'Register.html', {'form' : userform})