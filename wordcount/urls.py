
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('words',views.words,name="words"),
    path('count',views.count,name='count'),
    path('about',views.about,name='about'),
]
