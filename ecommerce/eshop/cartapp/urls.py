from . import views
from django.urls import path
app_name='cartapp'
urlpatterns=[
    path('add/<int:products_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:products_id>/',views.remove,name='remove'),
    path('full_remove/<int:products_id>/',views.full_remove,name='full_remove')
]