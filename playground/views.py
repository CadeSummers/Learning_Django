from django.shortcuts import render
#importing the http library from django
from django.http import HttpResponse


# Create your views here.
#view functions take in requests and return responses

#defining function to say hello, taking in a request
def say_hello(request):
    
    #returning a template named 'hello.html' found in our 'templates' folder
    return render(request, 'hello.html', {'name' : 'Cade'})
    

def say_goodbye(request):

    return HttpResponse('Goodbye!')


def homepage(request):

    return render(request, 'homepage.html')