from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name='home'),
    path("speak",views.speak,name ='speak'),
    path("speech_to_text/",views.speech_to_text,name='speech_to_text')
]