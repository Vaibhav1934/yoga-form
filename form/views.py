from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import info


# Create your views here.


def logout(request):
   
    return redirect('index')



    
def infox(request):

	try:
		if user=='O':
			messages.info(request, "Email Alerdy registered Edit Your Batch")
			
		else:
			messages.info(request, "Select Batch")
			
	       
		data=info.objects.filter(email=email)
		if request.method == 'POST':
			batch = request.POST['batch']
			info.objects.filter(email=email).update(batch=batch)
		
	
		
		return  render( request,'infox.html')
	except:
		return redirect('index')


def index(request):
	print(request.method)
	if request.method == 'POST':
		
        	first_name = request.POST['firstname'].lower()
        	last_name = request.POST['lastname'].lower()
        	global email
        	email = request.POST['email']
        	age= request.POST['age']    	
        	print(age,email,first_name ,last_name ,email)
        	if User.objects.filter(email=email).exists():
                	
                	
                	
                	print("old user")
                	
                	#infox(request,title='old')
                	global user
                	user="O"
                
                	
                	return redirect('infox')
        	
        	
        	else:
                	user = User.objects.create_user(username=email,email=email, first_name=first_name, last_name=last_name)
                	infodb=info.objects.create(email=email,age=age)
                	print(age,email,first_name ,last_name ,email)
                	infodb.save()
                	user.save()
                	
                	
                	print("new user")
                	#infox(request,title='new')
                	
                	
                
                	return redirect('infox')
        	
        	
        	return redirect('infox')
        	
        	
	return render(request,'index.html')
        


 
	

