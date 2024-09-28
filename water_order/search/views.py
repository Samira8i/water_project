from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import SearchForm
from .models import Product
from django.core.paginator import Paginator


def search_products(request):
    form = SearchForm()
    results = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)

            paginator = Paginator(results, 10)  # 10 товаров на странице
            page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
            page_obj = paginator.get_page(page_number)  # Получаем нужную страницу

            return render(request, 'search/search.html', {'form': form, 'page_obj': page_obj})

    return render(request, 'search/search.html', {'form': form, 'results': results})

    