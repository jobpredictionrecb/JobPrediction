from django.contrib import admin
from django.urls import path , include
from . import  settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('Home.urls','Home'),namespace='home')),
    path('prediction/',include(('Prediction.urls','Prediction'),namespace='prediction')),
    path('resumebuilder/',include(('ResumeBuilder.urls','ResumeBuilder'),namespace='resumebuilder')),
    path('register/',include(('accounts.urls','accounts'),namespace='accounts')),
    path('feedback/',include(('Feedback.urls','Feedback'),namespace='feedback')),
    path('contact/',include(('Contact.urls','Contact'),namespace='contact')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)