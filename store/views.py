from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product


class StoreListAndCategoryView(View):
    def get(self, request, category_slug=None):
        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category, is_available=True)
        else:
            category = None
            products = Product.objects.all().filter(is_available=True).order_by("product_name")

        paginator = Paginator(products, 6)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
        categories = Category.objects.all()

        context = {
            "products": paged_products,
            "product_count": product_count,
            "category": category,
            "categories": categories,
        }
        return render(request, 'store/store.html', context)


class ProductDetailView(View):
    def get(self, request, category_slug, product_slug):
        try:
            single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
            in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
            print(single_product)
        except Exception as e:
            raise e
        similar_products = Product.objects.filter(category=single_product.category)
        context = {
            "product": single_product,
            "in_cart": in_cart,
            "similar_products": similar_products,

        }
        return render(request, "store/product_detail.html", context)


def search(request):
    products = None
    product_count = None
    if 'keyword' in request.GET:
        keyword = request.GET["keyword"]
        print(keyword)
        if keyword:
            products = Product.objects.order_by("-created_date").filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword) |
                Q(category__category_name__icontains=keyword)
            )
            product_count = products.count()
    context = {
        "products": products,
        "product_count": product_count,
    }

    return render(request, 'store/store.html', context)




