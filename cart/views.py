from .models import Cart
from django.views.generic import DetailView


class CartDetailView(DetailView):
    """
    カートの詳細ページ
    """
    model = Cart
    template_name = 'cart/shopping_cart.html'