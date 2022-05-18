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

#take custom made object History from models.py
from .models import History


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

            #print("----------HERE---------")
            #print(username + ":" + password)

            user = authenticate(username=username, password=password)

            print("USER")
            print(user)
            print("ABOVE")

            #if the user exists
            if user is not None:

                #log them in
                login(request, user)

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


#def login(request):

#    return render(request, 'login.html')
#def playground(request):

#    return render(request, 'playgrond.html')