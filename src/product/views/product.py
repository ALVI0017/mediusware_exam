# from django.views import generic

# from product.models import Variant


# class CreateProductView(generic.TemplateView):
#     template_name = 'products/create.html'

#     def get_context_data(self, **kwargs):
#         context = super(CreateProductView, self).get_context_data(**kwargs)
#         variants = Variant.objects.filter(active=True).values('id', 'title')
#         context['product'] = True
#         context['variants'] = list(variants.all())
#         return context

from django.views import generic
from django.views.generic import ListView, CreateView

from product.models import Variant,Product,ProductVariantPrice,ProductVariant
from product.views.variant import BaseVariantView
from product.forms import ProductForm
from django.db.models import Q











class CreateProductView(generic.TemplateView):
  
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

   

class VariantCreateView(CreateProductView, CreateView):
    pass


def is_valid_queryparam(param):    
    return param != "" and param is not None

class ProductListView(ListView):
 
    model = Product
    context_object_name = 'products' 
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        pro_var_price =  ProductVariantPrice.objects.all() 
      
        context['variants'] = pro_var_price
        
        context['main_variant'] = Variant.objects.all()
        
        context['variants'] = ProductVariantPrice.objects.all()
        context['allvariants'] = ProductVariant.objects.all()
        
        context["title"]=self.request.GET.get("title","")
        context["variant"]=self.request.GET.get("variant","")
        context["price_from"]=self.request.GET.get("price_from","")
        context["price_to"]=self.request.GET.get("price_to","")
        context["date"]=self.request.GET.get("date","")
      
        return context


    

    def get_queryset(self):
        title_val=self.request.GET.get("title","")
        
        var_val=self.request.GET.get("variant","")
        
        price_from = self.request.GET.get("price_from","")
        price_to = self.request.GET.get("price_to","")
        
        
        startdate = self.request.GET.get("date","")
        
        product = Product.objects.all()     
        if is_valid_queryparam(title_val):
            product = Product.objects.filter(title__icontains=title_val)        

        if is_valid_queryparam(var_val):
            var = ProductVariantPrice.objects.filter(Q(product_variant_one_id=var_val)|Q(product_variant_two_id=var_val)|Q(product_variant_three_id=var_val)).values_list('product', flat=True)
            product = product.filter(Q(title__icontains=title_val) & Q(pk__in=var))
         
        if is_valid_queryparam(price_from):
            
            var = ProductVariantPrice.objects.filter(Q(price__gte=price_from)).values_list('product', flat=True)
            product = product.filter(Q(title__icontains=title_val) & Q(pk__in=var))
        
        if is_valid_queryparam(price_to):
            var = ProductVariantPrice.objects.filter(Q(price__lte=price_to)).values_list('product', flat=True)
            product = product.filter(Q(title__icontains=title_val) & Q(pk__in=var))
        if is_valid_queryparam(price_from) and is_valid_queryparam(price_to):
            var = ProductVariantPrice.objects.filter(Q(price__range=(price_from, price_to))).values_list('product', flat=True)
            product = product.filter(Q(title__icontains=title_val) & Q(pk__in=var))
            
        if is_valid_queryparam(startdate):
            var = ProductVariantPrice.objects.filter(Q(created_at__gte=startdate)).values_list('product', flat=True)
            product = product.filter(Q(title__icontains=title_val) & Q(pk__in=var))     
        
        
        
        if is_valid_queryparam(var_val) and is_valid_queryparam(price_from) and is_valid_queryparam(price_to) and is_valid_queryparam(startdate):
            
            var = ProductVariantPrice.objects.filter(Q(product_variant_one_id=var_val)|Q(product_variant_two_id=var_val)|Q(product_variant_three_id=var_val)|Q(price__range=(price_from, price_to))|Q(created_at__gte=startdate)).values_list('product', flat=True)
            product=Product.objects.filter(Q(title__icontains=title_val) & Q(pk__in=var))
            
        if is_valid_queryparam(var_val) and is_valid_queryparam(price_from) and is_valid_queryparam(price_to):  
        
            var = ProductVariantPrice.objects.filter(Q(product_variant_one_id=var_val)|Q(product_variant_two_id=var_val)|Q(product_variant_three_id=var_val)|Q(price__range=(price_from, price_to))).values_list('product', flat=True)
            product=Product.objects.filter(Q(title__icontains=title_val) & Q(pk__in=var))
            
        
        if is_valid_queryparam(var_val) and is_valid_queryparam(startdate):
            
            var = ProductVariantPrice.objects.filter(Q(product_variant_one_id=var_val)|Q(product_variant_two_id=var_val)|Q(product_variant_three_id=var_val)|Q(created_at__gte=startdate)).values_list('product', flat=True)
            product=Product.objects.filter(Q(title__icontains=title_val) & Q(pk__in=var))
        
        
 
        return product
    
    
  