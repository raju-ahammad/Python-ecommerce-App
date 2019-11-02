from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category, ProductImage
from django.shortcuts import redirect
from cart.forms import CartAddProductForm
from blog.models import BlogPost

class HomePageView(ListView):
    model   = Product
    template_name = 'product/home.html'
    context_object_name = 'product_list'


    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['featured'] = Product.objects.filter(featured=True).order_by('-created')[:3];
        context['inspired'] = Product.objects.filter(inspired=True).order_by('-created')[:8];
        context['new_product'] = Product.objects.filter(active=True).order_by('-created')[:4];
        context['created']   = BlogPost.objects.order_by('-created')[:3];
        return context




class DetailProductView(DetailView):
    model   = Product
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailProductView, self).get_context_data(*args, **kwargs)
        context['images'] = ProductImage.objects.filter(product=self.object.id)
        context['cart_product_form'] = CartAddProductForm

        return context


class ProductListView(ListView):
    model   = Product
    template_name = 'product/shop.html'
    context_object_name = 'product_list'
    paginate_by  = 9

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['active'] = Product.objects.filter(active=True).order_by('-created')
        return context


class CategoryView(ListView):
    model  = Product
    template_name  = 'product/category.html'
    context_object_name = 'category_list'
    paginate_by  = 9


    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryView, self).get_context_data(**kwargs)
        # Add in the category
        context['category'] = self.category
        return context


def contact(request):
    return render(request, 'product/contact.html')
