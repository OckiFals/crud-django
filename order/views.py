from django.http import HttpResponse
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

    context = {
        'beers': beers,
        'beers_count': beers_count,
        'order_items': json.loads(request.session['order'])
    }
    return render_to_response('order/orderall.html', context, context_instance=RequestContext(request))


@login_required
@csrf_exempt  # disable csrf protection on this func.
def addbeer(request):
    form = OrderBeerForm(request.POST)
    _dict = {
        'beer_id': form.data['beer_id'],  # FIXME why form.cleaned_data is undefined?
        'beer_name': form.data['beer_name'],
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
