from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'cart/detail.html', {'cart': cart})

# def create_checkout_session(request):
#     cart = Cart(request)
#     line_items = []

#     for item in cart:
#         line_items.append({
#             'price_data': {
#                 'currency': 'usd',
#                 'product_data': {
#                     'name': item['product'].name,
#                 },
#                 'unit_amount': int(item['price'] * 100),  
#             },
#             'quantity': item['quantity'],
#         })

#     try:
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=line_items,
#             mode='payment',
#             success_url=request.build_absolute_uri('/success/'),
#             cancel_url=request.build_absolute_uri('/cancel/'),
#         )
#         return redirect(session.url, code=303)
#     except Exception as e:
#         return render(request, 'cart/payment_error.html', {'error': str(e)})

# def payment_success(request):
#     return render(request, 'payment_success.html')

# def payment_cancel(request):
#     return render(request, 'payment_cancel.html')