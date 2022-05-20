from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

#import login functionality
from django.contrib.auth import login, authenticate
#take the new user form from forms.py
from .forms import NewUserForm
#import message functionalilty
from django.contrib import messages
#import datetime field from .models.fields
#from django.db.models.fields import DateTimeField

#import datetime from datetime (to use datetime.now())
from datetime import datetime


#take custom made object History from models.py
from .models import History

#import the entirety of the request module
import requests


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

#function to define registration request
def register_request(request):

    #if posting 
	if request.method == "POST":
        
        #fill form object with Post information
		form = NewUserForm(request.POST)

        #if valid form
		if form.is_valid():

            #save the user
			user = form.save()

            #create login request
			login(request, user)

            #inform user of successful registration
			messages.success(request, "Registration successful." )

            #and redirect to homepage
			return redirect("/")

        #otherwise inform failure
		messages.error(request, "Unsuccessful registration. Invalid information.")
    
    #if request method is ostensibly GET

    #create empty form
	form = NewUserForm()

    #return render of register.html
	return render (request=request, template_name="register.html", context={"register_form":form})

#define login function
def login_request(request):

    #if posting 
    if request.method == "POST":
        
        #fill form object with Post information
        form = AuthenticationForm(request, data=request.POST)

        print("Attempted Login")

        if form.is_valid():

            print("VALID")
            #authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            print("USER")
            print(user)

            #if the user exists
            if user is not None:

                #log them in
                login(request, user)

                #save a variable data as the request.POST values
                data = request.POST

                print("Data")
                #print(data['username']) #will need this for forms
                #print(data['password']) #will need this for forms
                print(request.path_info) #will need this
                #print()

                #createa timestamp for the request
                timestamp = datetime.now()

                #creation of list of keys to be passed to the_eye
                #form session_id, category, name, data, timestamp 
                event_values = [request.session.session_key, "User Auth & Registry", "Login", data, str(timestamp)]

                #calling the_eye
                the_eye(request, event_values, event="login")

                #inform user of success
                messages.info(request, f"You are now logged in as {username}.")

                #return redirect
                return redirect("/playground/hello/", context = {'name' : str(username)})

                #return render(request, "/hello.html", {'name' : str(username)})

            #otherwise inform failure    
            else:

                messages.error(request, "Invalid username and/or password.")

        #if invalid form, inform failure
        else:   

            messages.error(request, "Invalid username and/or password.")
    
    #otherwise, if request method is ostensibly GET

    #get an empty form
    form = AuthenticationForm()

    #return render of login.html
    return render(request, 'login.html', {'login_form' : form})


def history(request):

   #return an instance of history rendered with hello.html
   return render(request, 'hello.html', {'name' : History()})


#define function the_eye to track information from cookie

#define a function that takes in a request and an event, which must be a string (to serve as value in key value pair), and the keys, the actual value to fill the request at that index with.
#function 'the_eye' will be called on event request
def the_eye(request, event_values, event: str): #add argument for session id?

    #session is a dictionary-like object

    #session_key refers to the sessionid in Django
    data = request.POST
    path = request.path_info
    #
    #
    timesamp = datetime.now()

    #create a list of all required data value's in dict-like object
    key_list = ["session_id", "category", "name", "data", "timestamp"]

    #if the length of keys doesn't match the length of format list
    if len(event_values) != 5:
        
        #report failure
        print("The eye failed! Try again.")
        return -1

    #declaration of an event dictionary
    event_dict = {key_list[i]: event_values[i] for i in range(5)}

    print("Session_key")
    print(event_values[0])

    print("Event_Dict: ")
    print(event_dict)

    #TODO zip format_list to keys

    #append the session with an event, correlated to the above dict-like object
    request.session[event] = event_dict

    #printcheck
    #print(request.session[event["session_id"]])

    #for item, key in request.session:
    #    print(item)
    #    print(key)

    #some final return, which avoids races conditions, collisions, and can handle multiple inputs at once
    

