from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/register/login/')
def predict(request):
    return render(request,'Prediction/predict.html' )
