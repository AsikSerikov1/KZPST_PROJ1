# forms.py
from django import forms
from .models import City


class CityForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='',
        required=True,
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
    )
