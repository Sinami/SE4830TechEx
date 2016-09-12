from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse

from .forms import GroupInfoForm
from .models import GroupInfo

def index(request):
	#group = GroupInfo.objects.order_by('id')[:5]
	#context = {'group': group}
	#return render(request, 'groupTracker/index.html', context)
	if request.method == "POST":
		form = GroupInfoForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('groupTracker:submit',pk=post.pk)
	else:
		form = GroupInfoForm()
	return render(request, 'groupTracker/index.html', {'form':form})


def details(request,user_id):
	group = get_object_or_404(GroupInfo,id=user_id)
	return render(request, 'groupTracker/detail.html', {'group': group})

def showAll(request):
	#groups = get_object_or_404(GroupInfo, pk=1)
	groups = GroupInfo.objects.order_by('id')
	context = {'groups':groups}
	return render(request, 'groupTracker/showAll.html', context)

def submit(request,pk):
#	form = GroupInfoForm()
	post = get_object_or_404(GroupInfo, pk = pk)
	return render(request, 'groupTracker/details.html', {'post': post})	
