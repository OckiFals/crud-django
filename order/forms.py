from django import forms


class OrderBeerForm(forms.Form):
    beer_id = forms.IntegerField(label=u'beer', show_hidden_initial=False)
    beer_qty = forms.IntegerField(label=u'quantity', min_value=1)