from . import views
from django.urls import path
app_name='eshopapp'
urlpatterns=[
    path('',views.all_product_cat,name='all_product_cat'),
    path('<slug:c_slug>/',views.all_product_cat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodetail'),
]