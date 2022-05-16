from django.db import models
from django.urls import reverse


# Create your models here.

class ProductType(models.Model):
    name =  models.TextField()
    def __str__(self):
        return f' {self.name}'


class Production(models.Model):
    code = models.TextField()
    name = models.TextField()
    price = models.IntegerField(default=0)
    soluong = models.IntegerField(default=0)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=False, null=True)
    

    def __str__(self):
        return f'Ma hang hoa: {self.id}, Ten mat hang: {self.name}, Loai hang hoa: {self.producttype}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

