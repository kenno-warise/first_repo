from django.db import models
from django.contrib.auth.models import User # Djangoでは推奨していない
from django.conf import settings
from mamazon.models import Product

User = settings.AUTH_USER_MODEL # 推奨されている方法


class Cart(models.Model):
    """
    ショッピングカート
    user: ユーザー名
    products: 商品
    total: 合計金額
    created: カートが作られた日
    updated: カートが追加された日
    """
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2) # 小数点を使えるフィールド
    created = models.DateTimeField(auto_now_add=True) # 作成された時間
    updated = models.DateTimeField(auto_now=True) # 更新されたら変更