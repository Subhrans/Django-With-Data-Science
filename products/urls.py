from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path('', views.index, name="home"),
    path('live/',views.live_video,name="live"),
]
