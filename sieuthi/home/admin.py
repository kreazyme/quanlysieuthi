from django.contrib import admin

from .models import Production
from .models import ProductType

# Register your models here.
admin.site.register(Production)
admin.site.register(ProductType)