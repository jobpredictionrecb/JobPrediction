from django.shortcuts import render
from .forms import FeedbackForm
from .models import FeedbackModel

def feedback_view(request):

    feed = FeedbackModel.objects.all()

    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            fform.save()

    fform = FeedbackForm()

    return render(request,'Feedback/feedback.html',{'fform':fform,'feed':feed})


