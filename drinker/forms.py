from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from drinker.models import Drinker


class RegistrationForm(ModelForm):
    username = forms.CharField(label=u'User Name')
    name = forms.CharField(label=u'Name')
    email = forms.EmailField(label=u'Email Address')
    password = forms.CharField(label=u'Password',
                               widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=u'Verify Password',
                                widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Drinker
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            "That username already taken, please select another"
        )

    def clean(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']

        if password != password1:
            raise forms.ValidationError("Passwords did not match")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Username')
    password = forms.CharField(label=u'Password',
                               widget=forms.PasswordInput(render_value=False))


class EditProfile(forms.Form):
    name = forms.CharField(label=u'Name')
    email = forms.EmailField(label=u'Email Address')
    birthday = forms.DateField(label=u'Birthday')

    class Meta:
        model = Drinker
        exclude = ('user',)    