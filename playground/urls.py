from django.urls import path
from . import views

#This file contains the url configurations matched with the 'views' or request functionallities located in views.py.
#Create pages rendered from html or which are responses in views.py

#URLConf
urlpatterns = [

    #configuration
    path('hello/', views.say_hello),

    path('goodbye/', views.say_goodbye),

    path('homepage/', views.homepage),

    path('history/', views.history),

    path('register/', views.register_request),

    path('login/', views.login_request)

    #path('playground/', views.playground)

]