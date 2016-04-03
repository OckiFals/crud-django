from django.shortcuts import render_to_response
from django.template import RequestContext
from beer.models import Beer, Brewery
from drinker.forms import LoginForm


def home(request):
    return render_to_response('index.html')


def BeersAll(request):
    beers = Beer.objects.all().order_by('name')[:5]
    beers_count = Beer.objects.count()

    if request.method == "POST":
        form_login = LoginForm(request.POST)
    else:
        form_login = LoginForm()

    context = {
        'beers': beers,
        'beers_count': beers_count,
        'form': form_login
    }
    return render_to_response('beer/beersall.html', context, context_instance=RequestContext(request))


def SpecificBeer(request, beerslug):
    beer = Beer.objects.get(slug=beerslug)

    if request.method == "POST":
        form = LoginForm(request.POST)
    else:
        form = LoginForm()

    context = {
        'beer': beer,
        'form': form
    }
    return render_to_response('beer/singlebeer.html', context, context_instance=RequestContext(request))


def BrewerysAll(request):
    brewerys = Brewery.objects.all()

    if request.method == "POST":
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    context = {
        'brewerys': brewerys,
        'form': form
    }
    return render_to_response('beer/brewerysall.html', context, context_instance=RequestContext(request))


def SpecificBrewery(request, breweryslug):
    brewery = Brewery.objects.get(slug=breweryslug)
    beers = Beer.objects.filter(brewery=brewery)

    if request.method == "POST":
        form_login = LoginForm(request.POST)
    else:
        form_login = LoginForm()

    context = {
        'beers': beers,
        'form': form_login
    }
    return render_to_response('beer/singlebrewery.html', context, context_instance=RequestContext(request))
