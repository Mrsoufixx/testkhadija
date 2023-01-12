from django.db import models
from django.contrib.auth import get-user-model

user = get-user-model()

class profile(models.model):
   user = models.charfield(max-length=20)
   bio = models.charfield(max-length=40)
   location = models.charfield(max-lenght=80)
    
    
 class post(models,model):
    author = models.foreignkey(profile, on-delete=models.CASCADE) 
    
    titlle = models.charfield(max-length=200)
    
    Text = models.textfield   
    
    created date = models.datetimefield(auto-now-add=true)
    
    updated-date = models.datetimefield(auto-now=true)

    








