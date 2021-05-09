from django.shortcuts import render
from .models import Product,Purchase
import pandas as pd
# Create your views here.
def index(request):
    qs1=pd.DataFrame(Product.objects.all().values()).to_html
    qs2=pd.DataFrame(Purchase.objects.all().values()).to_html
    context={
        'product':qs1,
        'purchase':qs2,
    }

    return render(request,'products/index.html',context)
