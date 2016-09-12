from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

from .forms import GroupInfoForm, GroupInfoDeleteForm
from .models import GroupInfo

def index(request):
	#group = GroupInfo.objects.order_by('id')[:5]
	#context = {'group': group}
	#return render(request, 'groupTracker/index.html', context)
	if request.method == "POST":
		if 'submit' in request.POST:
			form = GroupInfoForm(request.POST)
			if form.is_valid():
				post = form.save()
				return redirect('groupTracker:submit',pk=post.pk)
		elif 'delete' in request.POST:
			searchStr = GroupInfoDeleteForm(request.POST)
			if searchStr.is_valid():
				#logger.error(searchStr)
				l_name = searchStr.cleaned_data['last_name']
				g_name = searchStr.cleaned_data['group_name']
				GroupInfo.objects.filter(last_name=l_name).filter(group_name=g_name).delete()
				return redirect('groupTracker:delete')
		elif 'find' in request.POST:
			searchStr = GroupInfoFindForm(request.POST)
			if searchStr.is_valid():
				c_name = searchStr.cleaned_data['class_name']
				records = GroupInfo.objects.filter(class_name=c_name)
				return redirect('groupTracker:details', pk=records.pk)
	else:
		form = GroupInfoForm()
		deleteform = GroupInfoDeleteForm()
	return render(request, 'groupTracker/index.html', {'form':form, 'deleteform':deleteform})


def details(request,pk):
	group = get_object_or_404(GroupInfo,id=pk)
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

def delete(request):
	return render(request, 'groupTracker/delete.html')
