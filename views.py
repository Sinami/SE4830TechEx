from django.shortcuts import render
from django.http import HttpResponse
from .forms import GroupInfoForm
from .models import GroupInfo

def index(request):
	#group = GroupInfo.objects.order_by('id')[:5]
	#context = {'group': group}
	#return render(request, 'groupTracker/index.html', context)
	if request.method == "POST":

	form = GroupInfoForm()
	return render(request, 'groupTracker/index.html', {'form':form})	


def details(request,user_id):
	group = get_object_or_404(GroupInfo,id=user_id)
	return render(request, 'groupTracker/detail.html', {'group': group})

def showAll(request,id):
	return HttpResponse("Show %s." % id)

def submit(request):
#	form = GroupInfoForm()
	return HttpResponse("Work in Progress- SUbmit")	
