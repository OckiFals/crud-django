from django.contrib import admin
from django.conf.urls import url, include
import beer.views
import drinker.views
import order.views

# from django.views.generic import direct_to_template
from people.views import PeopleList, ViewPerson, NewPerson, KillPerson, \
    EditPerson, ViewCategory, EditCategory, DeleteCategory, \
    CategoryDetail, NewCategory, CategoryList

admin.autodiscover()

person_urls = [
    url(r'^$', ViewPerson.as_view(), name='person_detail'),
    url(r'^Update$', EditPerson.as_view(), name='person_update'),
    url(r'^Delete$', KillPerson.as_view(), name='person_delete'),
]

category_urls = [
    url(r'^$', ViewCategory.as_view(), name='category_detail'),
    url(r'^Alternate$', CategoryDetail.as_view(), name='category_detail_alt'),
    url(r'^Update$', EditCategory.as_view(), name='category_update'),
    url(r'^Delete$', DeleteCategory.as_view(), name='category_delete'),
]

order_urls = [
    url(r'^$', order.views.showitems, name='order_show'),
    url(r'^add/$', order.views.addbeer, name='order_beer'),
]

urlpatterns = [
    url(r'^$', beer.views.home, name='home'),
    url(r'^people$', PeopleList.as_view(), name='people_list'),
    url(r'^(?P<slug>[\w-]+).person/', include(person_urls)),
    url(r'^NewPerson$', NewPerson.as_view(), name='person_add'),
    url(r'^Categories$', CategoryList.as_view(), name='category_list'),
    url(r'^(?P<slug>[\w-]+).cat/', include(category_urls)),
    url(r'^NewCategory$', NewCategory.as_view(), name='category_add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^servers/', include('servers.urls')),

    # orders app
    url(r'^order/', include(order_urls)),

    # beers app
    url(r'^beers/$', beer.views.BeersAll, name='beers_all'),
    url(r'^beers/(?P<beerslug>.*)/$', beer.views.SpecificBeer, name='single_beer'),
    url(r'^brewerys/$', beer.views.BrewerysAll, name='brewerys_all'),
    url(r'^brewerys/(?P<breweryslug>.*)/$', beer.views.SpecificBrewery),
    url(r'^register/$', drinker.views.drinker_registration, name='drinker_register'),
    url(r'^profile/$', drinker.views.profile, name='drinker_profile'),
    url(r'^profile/settings/$', drinker.views.edit_profile, name='drinker_setting'),
    url(r'^login/$', drinker.views.login_request, name='drinker_login'),
    url(r'^logout/$', drinker.views.logout_request, name='drinker_logout'),
]
