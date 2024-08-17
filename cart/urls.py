from django.urls import path
from . import views

app_name = 'cart'




urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    # path('success/', views.payment_success, name='payment_success'),
    # path('cancel/', views.payment_cancel, name='payment_cancel'),
]