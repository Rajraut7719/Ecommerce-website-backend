from django.db import models
from base.models import BaseModel
from tinymce.models import HTMLField
class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to="categories")

    def __str__(self):
        return self.category_name

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    price=models.IntegerField()
    product_description=HTMLField()
    

    def __str__(self):
        return self.product_name


class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.product)

