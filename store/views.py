from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from category.models import Category
from store.models import Product


class StoreListAndCategoryView(View):
    def get(self, request, category_slug=None):
        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category, is_available=True)
        else:
            products = Product.objects.all().filter(is_available=True).order_by("id")

        paginator = Paginator(products, 6)
        page = self.kwargs.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()

        context = {
            "products": paged_products,
            "product_count": product_count
        }
        return render(request, 'store/store.html', context)




