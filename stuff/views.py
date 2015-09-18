import django.http import JsonResponse
from django.contrib.auth import hashers
from django import db
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from stuff import models

def creat_user(request):
	if request.method != 'POST': 
		return _error_response(request, 'must make POST request") 
	if 'first_name' not in request.POST or 'last_name' not in request.POST or 'password' not in request.POST or 'username' not in request.POST or 'type_of_user' not in request.POST:  
	return _error_response(request, "missing required fields")
	
	u = models.User(username=request.POSt['username],
		first_name = request.post['first_name'],
		last_name = request.post['last_name'],
		password = hashers.make_password(request.POST['password']),
		date_joined = datetime.datetime.now()
	)
	try:
		u.save()
	except db.Error:
		return _error_response(request, "db error")
	return _success_response(request, {'user_id': u.pk})

def userlogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponse("Login successful")
			else:
				return HttpResponse("Failed Login")
		else:
			return HttpResponse("Wrong login info.")
	else:
		return _error_response(request, "must make POST requesT")
@login_required
def userlogout(request):
	logout(request)	
	return HttpResponse("logged out") 
