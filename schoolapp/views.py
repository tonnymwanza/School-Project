import profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Question
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .form import UserEditForm, QuestionForm
from .models import Profile
from .decorators import allowed_users
# Create your views here.

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

@login_required(login_url="login")
def adminstrator(request):
    return render(request, "adminstrator.html")

@login_required(login_url="login")
@allowed_users(allowed_roles=['Teacher'])
def teachers(request):
    return render(request, "teachers.html")

@login_required(login_url="login")
@allowed_users(allowed_roles=['Student'])
def students(request):
    obj = Question.objects.all()
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = Question.objects.create(
            question = form.cleaned_data["question"],
            answer_one = form.cleaned_data["answer_one"],
            answer_two = form.cleaned_data["answer_two"],
            answer_three = form.cleaned_data["answer_three"],
            answer_four = form.cleaned_data["answer_four"]
            )
            messages.success(request, "Assignment successfully submitted")
        else:
            form = QuestionForm()
    context = {
        "form" : form,
        "obj": obj
    }
    return render(request, "students.html", context)

def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        emailaddress = request.POST["emailaddress"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2: 
           if User.objects.filter(username = username).exists():
               messages.info(request, "the username is already taken!!!")
               return redirect("register")
           elif User.objects.filter(email = emailaddress).exists():
               messages.info(request, "the email already exists. try using another one!!!")
               return redirect("register")
           else:
               user = User.objects.create_user(first_name = firstname, last_name = lastname, email = emailaddress, username = username, password = password)
               user.save();
               Profile.objects.create(user=user)
               return redirect("login")
        else:
            messages.info(request, "the passwords do not match. Try again!!!")
            return redirect("register")
    
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('students')
        else:
            messages.info(request, "Username or Password incorrect. Try again")
            return redirect("login")
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

def success(request):
    return render(request, "success.html")

def password_change(request):
    form = PasswordChangeForm(user=request.user, data= request.POST)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect("success")
    context = {
        "form": form
    }
    return render(request, "password_change.html", context)

def student_profile(request):
    return render(request, "student_profile.html")

def logout(request):
    auth.logout(request)
    return render(request, "logout.html")

def correct_choice(request):
    return render(request, "students.html")

@login_required(login_url=login)
def edit(request):
    user_form = UserEditForm(instance=request.user)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Profile has been updated successfully")
        else:
            user_form = UserEditForm(instance=request.user)          
    return render(request, "edit.html", {"user_form":user_form})