from django.shortcuts import render



def Index(request):
	""" Home page for this project"""
 
	return render(request, 'index.html')