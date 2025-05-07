from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = 'Registration Successful'
            message = f"Hello {user.username},\n\nThank you for registering. Here are your details:\n\nUsername: {user.username}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Registration successful! Confirmation email sent.')
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})