from django.shortcuts import render

simple_variable = 0

def home_view(request):
    global simple_variable
    simple_variable = simple_variable + 1
    return render(request,'Home/home.html',{'pop':simple_variable})
