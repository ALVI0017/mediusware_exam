from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput,ChoiceField

from product.models import *


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            
            'title': TextInput(attrs={'class': 'form-control'}),
            'sku': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }

# class ProductImageForm(ModelForm):
#     class Meta:
#         model = Variant
#         fields = '__all__'
#         widgets = {
#             'title': TextInput(attrs={'class': 'form-control'}),
#             'description': Textarea(attrs={'class': 'form-control'}),
#             'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
#         }
class ProductVariantForm(ModelForm):
    class Meta:
        model = ProductVariant
        fields =  ['variant', 'variant_title']

        widgets = {
            'variant_title': TextInput(attrs={'class': 'form-control'}),
            'variant': TextInput(attrs={'class': 'form-control'}),
            # 'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }