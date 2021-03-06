from django.shortcuts import render, redirect
from django.contrib.auth import login

from . forms import UserRegistrationForm

# Create your views here.

def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserRegistrationForm()
    else:
        # Process completed form.
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page.
            login(request, new_user)
            return redirect('blog_QA:index')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)