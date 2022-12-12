from django.db import models

# Create your models here.

class info(models.Model):
	
	email=models.EmailField(max_length=254)
	age=models.IntegerField()
	date =  models.DateField(auto_now_add=True)
	batch=models.CharField(max_length=10)
	fee=models.CharField(max_length=10,default="not paid")
	

    
   
    
    
