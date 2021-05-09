from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd


# Create your views here.
def index(request):
    qs1 = pd.DataFrame(Product.objects.all().values())
    qs4 = pd.DataFrame(Product.objects.all().values()).to_html
    qs2 = pd.DataFrame(Purchase.objects.all().values()).to_html
    qs3 = pd.DataFrame(Purchase.objects.all().values())
    qs1['product_id'] = qs1['id']
    merged = pd.merge(qs1, qs3, on='product_id').drop(['id_x', 'date_x'],axis=1).to_html
    context = {
        'product': qs4,
        'purchase': qs2,
        'merged': merged,
    }

    return render(request, 'products/index.html', context)
