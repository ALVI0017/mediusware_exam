from django.contrib import admin

# Register your models here.
from product.models import *

# Register your models here.
admin.site.register(Variant)
admin.site.register(Product)

admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
