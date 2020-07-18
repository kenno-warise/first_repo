from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'


class ProductListView(ListView):
    """
    商品のリストを表示
    """
    model = Product
    template_name = 'mamazon/list.html'

    """
    商品の検索機能
    """
    def get_queryset(self):
        queryset = Product.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains=qs)
        return queryset


class ProductDetailView(DetailView):
    """
    商品の詳細ページ
    """
    model = Product
    template_name = 'mamazon/detail.html'