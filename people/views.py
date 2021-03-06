from django.views.generic.list import ListView
from people.models import Category, Person
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from people.forms import CategoryForm, PersonForm
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


class CategoryMixin(object):
    model = Category

    @staticmethod
    def get_context_data(**kwargs):
        kwargs.update({'object_name': 'Category'})
        return kwargs


class CategoryFormMixin(CategoryMixin):
    form_class = CategoryForm
    template_name = 'people/object_form.html'


class CategoryList(CategoryMixin, ListView):
    template_name = 'people/object_list.html'


class CategoryDetail(CategoryMixin, DetailView):
    pass


class NewCategory(CategoryFormMixin, CreateView):
    pass


class EditCategory(CategoryFormMixin, UpdateView):
    pass


class DeleteCategory(CategoryMixin, DeleteView):
    template_name = 'people/object_confirm_delete.html'

    def get_success_url(self):
        return reverse('category_list')


class PersonMixin(object):
    model = Person

    @staticmethod
    def get_context_data(**kwargs):
        kwargs.update({'object_name': 'Person'})
        return kwargs


class PersonFormMixin(PersonMixin):
    form_class = PersonForm
    template_name = 'people/object_form.html'


class PeopleList(PersonMixin, ListView):
    template_name = 'people/object_list.html'


class ViewPerson(PersonMixin, DetailView):
    pass


class NewPerson(PersonFormMixin, CreateView):
    pass


class EditPerson(PersonFormMixin, UpdateView):
    pass


class KillPerson(PersonMixin, DeleteView):
    template_name = 'people/object_confirm_delete.html'

    def get_success_url(self):
        return reverse('people_list')


class ViewCategory(PersonMixin, ListView):
    template_name = 'people/object_list.html'

    def __init__(self, **kwargs):
        super(ViewCategory, self).__init__(**kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])

    def get_queryset(self):
        return super(ViewCategory, self).get_queryset().filter(category=self.category)
