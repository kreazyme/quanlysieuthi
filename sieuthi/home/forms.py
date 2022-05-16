from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm

from .models import ProductType, Production


class ProductionForm(ModelForm):
    code = forms.CharField(
        label='MSSP',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mã số sản phẩm'
            }
        )
    )
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Tên sản phẩm : '
            }
        )
    )
    price = forms.CharField(
        initial='100000',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Giá tiền : '
            }
        )
    )
    class Meta:
        model = Production
        fields = [
            'code',
            'name',
            'producttype',
            'price'
        ]

class ProducttypeForm(ModelForm):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Tên loại hàng : '
            }
        )
    )
    class Meta:
        model = ProductType
        fields = [ 
            'name'
        ]