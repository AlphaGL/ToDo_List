# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import PasswordResetForm

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            new_password = form.cleaned_data.get('new_password1')
            
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change if needed
            messages.success(request, 'Your password has been successfully updated!')
            return redirect('login')  # Redirect to the login page or any other page
    else:
        form = PasswordResetForm()
    return render(request, 'reset/reset_password.html', {'form': form})
