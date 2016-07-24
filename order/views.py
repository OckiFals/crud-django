from django.http import HttpResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from beer.models import Beer
from order.forms import OrderBeerForm
import json


@login_required
def showitems(request):
    beers = Beer.objects.all().order_by('name')[:5]
    beers_count = Beer.objects.count()
    order_items = {}
    
    if 'order' in request.session:
        order_items = json.loads(request.session['order'])

    context = {
        'beers': beers,
        'beers_count': beers_count,
        'order_items': order_items
    }
    return render_to_response('order/orderall.html', context, context_instance=RequestContext(request))


@login_required
@csrf_exempt  # disable csrf protection on this func.
def addbeer(request):
    form = OrderBeerForm(request.POST)
    _dict = {
        'beer_id': form.data['beer_id'],  # FIXME why form.cleaned_data is undefined?
        'beer_name': form.data['beer_name'],
        'beer_slug': form.data['beer_slug'],
        'beer_qty': form.data['beer_qty']
    }

    if request.session.get('order') is None:
        request.session['order'] = json.dumps([_dict])
    else:
        temp_sess = json.loads(request.session['order'])

        for index, sess in enumerate(temp_sess):
            if sess['beer_id'] == _dict['beer_id']:
                temp_sess[index]['beer_qty'] = (
                    int(sess['beer_qty']) + int(_dict['beer_qty'])
                )
                break
        else:
            temp_sess.append(_dict)

        request.session['order'] = json.dumps(temp_sess)

    return HttpResponse(json.dumps(_dict), content_type="application/json")


@login_required
@csrf_exempt
def deletebeer(request):
    temp_sess = json.loads(request.session['order'])
    delete = QueryDict(request.body)
    beer_id = delete.get('beer_id')

    for index, sess in enumerate(temp_sess):
        if sess['beer_id'] == beer_id:
            del temp_sess[index]
            request.session['order'] = json.dumps(temp_sess)
            data = {
                'status': 'Ok',
                'message': 'Beer order with id=' + beer_id + ' has been successfully removed'
            }
            break
    else:
        data = {
            'status': 'NotFound',
            'message': 'Beer order with id=' + beer_id + ' not found'
        }

    return HttpResponse(json.dumps(data), content_type="application/json")
