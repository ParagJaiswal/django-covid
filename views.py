from django.shortcuts import render
from django.http import HttpResponse
def check(request):
	return render(request,'covid/covidcheck.html')

def agecheck(request):
	#global x
	#if request.method=='post':
	x =request.POST.get('r1')
	if x=='<60':
		y = "Your age is less then 60"
		return render(request,'covid/symptomcheck.html',{"key":y})
	if x=='>=60':
	 y = "Your age is greater or equal to 60"
	 return render(request,'covid/diseases.html',{"key":y})

def young(request):
	sym = request.POST.getlist('chk[]')
	d=0
	sad = ''
	for j in sym:
	 d= d+1
	 sad = sad +j

	if sad=='none':
		m = "Good"
	elif d==1:
		m = "Dont Worry"
	elif d==2:
		m = "Stay Safe"
	elif d==3:
		m = "Critical"
	elif d==4:
		m="Serious"
	elif d>=5:
		m = "god knows"

	return render(request,'covid/symptomcheck.html',{"health":m})

def old(request):
	sym = request.POST.getlist('chk[]')
	d=0
	sad = ''
	for j in sym:
	 d= d+1
	 sad = sad +j

	if sad=='none':
		m = "Dont Worry"
	elif d==1:
		m = "Stay Safe"
	elif d==2:
		m = "Critical"
	elif d==3:
		m = "Very Critical"
	elif d==4:
		m="Serious"
	elif d>=5:
		m = "Better Luck Next Time"

	return render(request,'covid/diseases.html',{"health":m})

	
	





