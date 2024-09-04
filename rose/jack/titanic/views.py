from django.shortcuts import render,redirect
from titanic.models import friends
from titanic.forms import friendsForm
# Create your views here.
def hisha(request):
	frd=friends.objects.all()
	return render(request,'hisha.html',{'s':frd})

def insert(request):
	frd=friendsForm()
	if request.method=="POST":
		frd=friendsForm(request.POST)
		if frd.is_valid():
			frd.save()
	return render(request,'insert.html',{'f':frd})

def update(request,id):
	frd=friends.objects.get(id=id)
	if request.method=="POST":
		frd=friendsForm(request.POST,instance=frd)
		if frd.is_valid():
			frd.save()
		return redirect('update/')
	return render(request,'update.html',{'u':frd})

def delete(request,id):
	frd=friends.objects.get(id=id)
	frd.delete()
	return redirect('/')
