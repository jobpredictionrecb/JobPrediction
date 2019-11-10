from django.urls import path

from .views import GeneratePDF
from . import views

from JobPrediction import  settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("",views.resume_view,name="resume"),
    path("pdf",GeneratePDF.as_view()),
    path("skill",views.skill_view,name="skill")

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)