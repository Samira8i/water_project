from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import WaterOrderForm

def order_water(request):
    if request.method == 'POST':
        form = WaterOrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'orders/order_summary.html', {'data': data})
    else:
        form = WaterOrderForm()

    return render(request, 'orders/order_form.html', {'form': form})
