from django.db import models


class Product(models.Model):
    """
    商品モデル
    name: 商品名
    price: 商品の値段
    description: 商品の説明
    thumbnail: 商品の写真
    """
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/') # 写真の保存先を指定