from django.contrib import admin
from product.models import Category,Product,ProductImage 
# Register your models here.
admin.site.register(Category)
icon_name='local_hospital'
admin.site.register(Product)
admin.site.register(ProductImage)