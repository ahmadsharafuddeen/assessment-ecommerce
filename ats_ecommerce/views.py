from django.shortcuts import render
# from store.models import Product
from django.views import View
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"
    # products = Product.objects.all().filter(is_available=True)