from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
from .forms import DataForm


# Create your views here.
def index(request):
    qs1 = pd.DataFrame(Product.objects.all().values())
    qs4 = pd.DataFrame(Product.objects.all().values()).to_html()
    qs2 = pd.DataFrame(Purchase.objects.all().values()).to_html()
    qs3 = pd.DataFrame(Purchase.objects.all().values())
    qs1['product_id'] = qs1['id']
    merged = pd.merge(qs1, qs3, on='product_id').drop(['id_y', 'date_x'], axis=1).rename(
        {'id_x': 'Id', 'date_y': 'Date'}, axis=1)
    if request.method == "POST":
        data_form=DataForm(request.POST)
        if data_form.is_valid():
            date_from=data_form.cleaned_data['date_from']
            date_to=data_form.cleaned_data['date_to']
            print("the date is",date_from)
    else:
        data_form = DataForm()
    context = {
        'product': qs4,
        'purchase': qs2,
        'merged': merged.to_html(),
        'data_form': data_form,
    }

    return render(request, 'products/index.html', context)
