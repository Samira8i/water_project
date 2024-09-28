# search/forms.py (или orders/forms.py)
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Название товара', max_length=100)
