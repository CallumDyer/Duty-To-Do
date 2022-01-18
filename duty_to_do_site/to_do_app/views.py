from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import To_Do_Point
from .models import PointForm

def to_do(request):
    latest_to_do_list = To_Do_Point.objects.order_by('-pub_date')[:5]
    context = {'latest_to_do_list': latest_to_do_list}
    return render(request, 'to_do_app/to_do.html', context)

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
        return render(request, 'to_do_app:error', {'form':form})

def error(request):
    return render(request, 'to_do_app/error.html')

    
    
    
