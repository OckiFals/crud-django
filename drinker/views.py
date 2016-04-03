from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from drinker.models import Drinker
from drinker.forms import RegistrationForm, LoginForm, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def drinker_registration(request):
    if request.user.is_authenticated() and not request.user.is_superuser:
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            drinker = Drinker()
            drinker.user = User.objects.get(username=form.data['username'])
            drinker.name = form.data['name']
            drinker.birthday = form.data['birthday']
            drinker.save()

            drinker = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            # auth for new drinker
            login(request, drinker)
            return HttpResponseRedirect('/beer/')
        else:
            return render_to_response('beer/registration.html', {'form': form},
                                      context_instance=RequestContext(request))
    else:
        ''' user is not submittinh the forms, show a blank registration page '''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('beer/registration.html', context,
                                  context_instance=RequestContext(request))


def login_request(request):
    if request.user.is_authenticated() and not request.user.is_superuser:
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            drinker = authenticate(username=username, password=password)
            if drinker is not None:
                login(request, drinker)
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return render_to_response(
                'beer/login.html',
                {'form': form},
                context_instance=RequestContext(request)
            )
    else:
        ''' user is not submitting the form '''
        form = LoginForm()
        return render_to_response(
            'beer/login.html',
            {'form': form},
            context_instance=RequestContext(request)
        )


@login_required
def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    user = request.user
    context = {'drinker': user.drinker}
    return render_to_response('beer/profile.html', context, context_instance=RequestContext(request))


@login_required
def edit_profile(request):
    if request.method == 'POST':
        drinker = request.user.drinker
        form = EditProfile(request.POST)
        context = {
            'drinker': drinker,
            'form': form
        }

        if form.is_valid():
            drinker.name = form.cleaned_data['name']
            drinker.email = form.cleaned_data['email']
            drinker.birthday = form.cleaned_data['birthday']
            drinker.save()
            messages.success(request, "Current submitted successfully")
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response(
                'beer/edit-profile.html', context,
                context_instance=RequestContext(request)
            )
    else:
        drinker = request.user.drinker
        form = EditProfile(initial={
            'name': drinker.name,
            'email': request.user.email,
            'birthday': drinker.birthday
        })
        context = {
            'drinker': drinker, 'form': form
        }
        return render_to_response(
            'beer/edit-profile.html', context,
            context_instance=RequestContext(request)
        )


def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/beers/')