
from django import forms

class WaterOrderForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Контактный телефон', max_length=15)
    address = forms.CharField(label='Адрес', widget=forms.Textarea)
    delivery_months = forms.ChoiceField(
        label='Количество месяцев доставки воды',
        choices=[
            ('1', 'Один месяц'),
            ('3', 'Три месяца'),
            ('6', 'Шесть месяцев'),
            ('12', 'Двенадцать месяцев'),
        ]
    )
    bottle_volume = forms.ChoiceField(
        label='Объём баллона воды',
        choices=[
            ('5', '5 литров'),
            ('10', '10 литров'),
            ('15', '15 литров'),
        ]
    )
