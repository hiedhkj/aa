from re import search
from django.views import View
from django.utils import timezone
from django.contrib import messages
from users.models import UserAccount
from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from books.models import Book
import random

def validate_password(password):
    if len(password) < 8:raise ValidationError("Too short, min 8 chars.")
    if not search("[a-z]", password):raise ValidationError("Need a lowercase letter.")
    if not search("[0-9]", password):raise ValidationError("Need a digit.")

class HomeView(View):
    def get(self, request):
        user_info = None
        if 'user_id' in request.session:
            try:
                user_info = UserAccount.objects.get(id=request.session['user_id'])
            except UserAccount.DoesNotExist:
                user_info = None
        books = list(Book.objects.all())
        random_books = random.sample(books, min(len(books), 15))
        expensive_books = Book.objects.order_by('-price')[:10]
        return render(request, 'home.html', {'user': user_info, 'random_books': random_books, 'expensive_books': expensive_books})

    def post(self, request):
        if 'signup' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            try:
                validate_email(email)
                validate_password(password)
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('home')

            if UserAccount.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            elif UserAccount.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            else:
                UserAccount.create_user(username, email, password)
                user = UserAccount.objects.get(email=email)
                user.last_login = timezone.now()
                user.is_active = True
                user.save()
                request.session['user_id'] = user.id
                messages.success(request, "Account created successfully.")
                return redirect('home')
        elif 'login' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = UserAccount.objects.get(email=email)
                if check_password(password, user.password):
                    user.last_login = timezone.now()
                    user.is_active = True
                    user.save()
                    request.session['user_id'] = user.id
                    messages.success(request, "Logged in successfully.")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid password.")
            except UserAccount.DoesNotExist:
                messages.error(request, "Email not registered.")
        return redirect('home')

def logout_view(request):
    if 'user_id' in request.session:
        try:
            user = UserAccount.objects.get(id=request.session['user_id'])
            user.is_active = False
            user.save()
        except UserAccount.DoesNotExist:
            pass
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def profile_view(request):
    return redirect('home')