# import email
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import render,redirect,HttpResponse
# from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm  # Adjust the import based on your project structure
from django.views.generic import View





# from django.views.generic import FormView
# from django.urls import reverse_lazy
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages
# # from .forms import ContactForm
# # Create your views here.


# from django.core.mail import send_mail

# from django.shortcuts import render
# from django.http import HttpResponse
# # from .forms import ContactForm







# from django.contrib.auth import authenticate,logout,login
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .forms import SignUpForm
# from .models import Product


# Create your views here (for login,logout,registration).


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request,('Welcome!'))
            return redirect('home')
        else:
            messages.success(request,('Username or Password incorrect. You Can Reset Password!!'))
            return redirect('login')
    else:
        return render(request, 'Home/login.html', {})

def logout_user (request):
    logout(request)
    # messages.success(request, 'Hello! logged out')
    return redirect('home')


def register_user (request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # password = form.cleaned_data['password2'] (optional)
            
            # Login User
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, 'You have registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while registering. Please Follow the instructions!')
            return redirect('register')
    else:
        return render(request, 'Home/register.html', {'form': form})






















# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
        
#         email_message = EmailMessage(
#             subject=f"{subject} from {name}",
#             body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}",
#             from_email=email,
#             to=['ibeawuchichukwugozirim@gmail.com'],  # Replace with your email
#         )

#         try:
#             email_message.send()
#             messages.success(request, 'Your message has been sent successfully.')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {e}')
        
#         return redirect('contact')  # Adjust the redirect as needed
    
#     return render(request, 'Home/contact.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)


        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
            

        #     message = form.cleaned_data['message']
        #     EmailMessage(
        #         'Contact Form Submission from {0}'.format(name),
        #         message,
        #         'form.resonse@example.com',
        #         ['ibeawuchichukwugozirim@gmail.com'],
        #         [],
        #         reply_to=[email]
        #     )
        #     EmailMessage.save()



    #     return render(request, 'Home/success.html')
    # else:
    #     form = ContactForm()

    # return render(request, 'Home/contact.html', {'form': form})

# def success(request):
#     return HttpResponse('Success')

# class ContactView(FormView):
#     template_name = 'Home/contact.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact')  # It's better to use reverse_lazy for URLs

#     def form_valid(self, form):
#         message = form.cleaned_data['message']
#         try:
#             send_mail(
#                 'Contact Form',
#                 message,
#                 email, # sender
#                 ['ibeawuchichukwugozirim@gmail.com'], # recipient
#                 fail_silently=False,
#             )
#         except Exception as e:
#             return HttpResponse(f"An error occurred: {e}")

#         return super().form_valid(form)
    

    ##############################################



        # return super().form_valid(form)
# class ContactView(FormView):
#     template_name = 'Home/contact.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact')
    
#     def form_valid(self, form):
#         # Process the form data
#         name = form.cleaned_data['name']
#         email = form.cleaned_data['email']
#         message = form.cleaned_data['message']

#         # Send email (this is just an example, configure your email settings in settings.py)
#         send_mail(
#             f'Message from {name}',
#             message,
#             email,
#             settings.EMAIL_HOST_USER,
#             ['ibeawuchichukwugozirim@gmail.com'],
#             fail_silently=False,
#         )

#         # Add a success message
#         messages.success(self.request, 'Thank you for your message. We will get back to you soon.')
#         return super().form_valid(form)

class Home(View):
    template_name = 'Home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class About(View):
    template_name = 'Home/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Blog(View):
    template_name = 'Home/blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class News(View):
    template_name = 'Home/news.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Recipe(View):
    template_name = 'Home/recipes.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)