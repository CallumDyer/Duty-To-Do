from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import To_Do_Point
from .models import PointForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('to_do_app:to_do'))
        else:
            return render(request, 'to_do_app/error.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'to_do_app/register.html', {'form':form})

def to_do(request):
    latest_to_do_list = To_Do_Point.objects.all().filter(user=request.user)
    context = {'latest_to_do_list': latest_to_do_list}
    return render(request, 'to_do_app/to_do.html', context)

def add(request):
    form = PointForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('to_do_app:to_do'))
    else:
        return render(request, 'to_do_app/error.html', {'form':form})
    
def edit(request, to_do_point_id):
    to_do_point = get_object_or_404(To_Do_Point, pk=to_do_point_id)
    return render(request, 'to_do_app/edit.html', {'to_do_point': to_do_point})

def edit_save(request, to_do_point_id):
    to_do_point = get_object_or_404(To_Do_Point, pk=to_do_point_id)
    form = PointForm(request.POST, instance=to_do_point)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('to_do_app:to_do'))
    else:
        return render(request, 'to_do_app/error.html', {'form':form})

def error(request):
    return render(request, 'to_do_app/error.html')

def delete(request, to_do_point_id):
    to_do_point = get_object_or_404(To_Do_Point, pk=to_do_point_id)
    form = PointForm(request.POST, instance=to_do_point)
    if form.is_valid():
        to_do_point.delete()
        return HttpResponseRedirect(reverse('to_do_app:to_do'))
    else:
        return render(request, 'to_do_app/error.html', {'form':form})
    

    
    
    
