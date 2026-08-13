from django.shortcuts import redirect, render

from .models import Register


def register(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not username or not email or not password:
            error_message = "All fields are required."
        elif password != confirm_password:
            error_message = "Passwords do not match."
        elif Register.objects.filter(email=email).exists():
            error_message = "A user with that email already exists."
        else:
            Register.objects.create(username=username, email=email, password=password, confirm_password=confirm_password)
            return redirect('login')
    return render(request, 'register-basic.html', {'error_message': error_message})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            register = Register.objects.get(email=email)
            if register.password == password:
                request.session['Register_id'] = register.id
                return redirect('index')
            error_message = "Invalid password."
        except Register.DoesNotExist:
            error_message = "User with this email does not exist."
        return render(request, 'login-basic.html', {'error_message': error_message})
    return render(request, 'login-basic.html')


def logout(request):
    request.session.flush()
    return redirect('index')


def index(request):
    is_logged_in = 'Register_id' in request.session
    if not is_logged_in:
        return render(request, 'index.html', {'is_logged_in': False})
    register = Register.objects.get(id=request.session['Register_id'])
    return render(request, 'index.html', {'register': register, 'is_logged_in': True})


def account(request):
    is_logged_in = 'Register_id' in request.session
    if 'Register_id' not in request.session:
        return redirect('login')
    register = Register.objects.get(id=request.session['Register_id'])
    return render(request, 'account.html', {'register': register, 'is_logged_in': is_logged_in})


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            Register.objects.get(email=email)
            return redirect('email-sent')
        except Register.DoesNotExist:
            return render(request, 'forgot-password-basic.html', {'error_message': "User with this email does not exist."})
    return render(request, 'forgot-password-basic.html')


def email_sent(request):
    return render(request, 'email-verification-basic.html')


def two_factor_auth(request):
    return render(request, 'two-step-verification-basic.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not email:
            return render(request, 'reset-password-basic.html', {'error_message': "Email is required."})
        if password != confirm_password:
            return render(request, 'reset-password-basic.html', {'error_message': "Passwords do not match."})
        try:
            register = Register.objects.get(email=email)
            register.password = password
            register.confirm_password = confirm_password
            register.save()
            return redirect('login')
        except Register.DoesNotExist:
            return render(request, 'reset-password-basic.html', {'error_message': "User with this email does not exist."})
    return render(request, 'reset-password-basic.html')
