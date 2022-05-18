from django.db import models

#import ContentType and Generic For
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

# Create your models here.

#User declaration
User = settings.AUTH_USER_MODEL

#Class containing history

class History(models.Model):

    #definite use attribute of history as models ForeignKey Method on User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #set variable content type to models.ForeignKey method which takes the ContentType as arg
    #on_delete will set models to NULL, 
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)

    #creation of an object to
    object_id = models.PositiveIntegerField() #assignment of integet id

    #content
    content_object = GenericForeignKey() #the actual object

    #set page viewership (automatically)
    viewed_on = models.DateTimeField(auto_now_add=True)


