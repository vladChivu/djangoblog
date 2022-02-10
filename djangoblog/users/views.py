from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # AND that's it! (will hash the password also)
            username = form.cleaned_data.get('username')
            # form.cleaned_data gets this data in a python variable type
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})