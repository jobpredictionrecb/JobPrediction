from django.shortcuts import render

def contact_view(request):
    return render(request,'Contact/contact.html')