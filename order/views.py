from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from order.forms import OrderBeerForm
import json


def showitems(request):
    return HttpResponse('tampil item')


@csrf_exempt  # disable csrf protection on this func.
def addbeer(request):
    form = OrderBeerForm(request.POST)
    _dict = {
        'beer_id': form.data['beer_id'], # FIXME why form.cleaned_data is undefined?
        'beer_name': form.data['beer_name'],
        'beer_qty': form.data['beer_qty']
    }
    
    if request.session.get('order') is None:
        request.session['order'] = json.dumps([_dict])
    else:
        temp_sess = json.loads(request.session['order'])
        temp_sess.append(_dict)
        request.session['order'] = json.dumps(temp_sess)

    return HttpResponse(request.session.get('order'), content_type="application/json")
