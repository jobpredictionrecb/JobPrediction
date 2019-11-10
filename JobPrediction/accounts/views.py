from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .forms import RegisterForm , LoginForm

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            msg = "Login Successful"
            return render(request,'Home/home.html',{'msg':msg})
            #return redirect("/")
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/register/login')
    else:
        lform = LoginForm()
        return render(request, 'Accounts/login.html',{'lform':lform})

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/register/registration')
                #err = "Username already taken"
                #return render(request, 'register.html', {'err': err})
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Username already taken")
                return redirect('/register/registration')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                msg = "Registration Successfull"
                lform = LoginForm()
                return render(request,'Accounts/login.html',{'lform':lform,'msg':msg})
                #return redirect('/register/login')
        else:
            messages.info(request, "Password Doesn't Matched")
            return redirect('/register/registration')

    else:
        rform = RegisterForm()
        return render(request,'Accounts/register.html',{'rform':rform})

def logout(request):
    auth.logout(request)
    return redirect('/')
