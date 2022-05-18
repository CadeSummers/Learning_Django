from django.contrib import admin

# Register your models here.

#importing the history model from our models to be avaialable on admin
from .models import History

#register history on admin site
admin.site.register(History)