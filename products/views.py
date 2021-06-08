from django.shortcuts import render, HttpResponse
from .models import Product, Purchase
import pandas as pd
from .forms import DataForm
import cv2 as cv


# Create your views here.
def index(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']
    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_x'], axis=1).rename(
            {'id_x': 'Id', 'date_y': 'date'}, axis=1)
        print(purchase_df.shape)
        print(product_df['date'][0])
        if request.method == "POST":
            data_form = DataForm(request.POST)
            if data_form.is_valid():
                date_from = data_form.cleaned_data['date_from']
                date_to = data_form.cleaned_data['date_to']
                print("the date is", date_from)

                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                print(df)
                df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                print(df2)
        else:
            data_form = DataForm()
    else:
        data_form = DataForm()
    context = {
        'product': product_df.to_html(),
        # 'purchase': qs3,
        'merged': df.to_html(),
        'data_form': data_form,
    }

    return render(request, 'products/index.html', context)


def live_video(request):
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret is not True:
            return HttpResponse("error")
        # cv.imshow('frame',frame)
        return render(request,'products/index.html',context={'image':frame})

        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
