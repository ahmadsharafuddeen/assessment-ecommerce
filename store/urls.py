from django.urls import path
from .views  import StoreListAndCategoryView, ProductDetailView, submit_review, search


app_name = "store"
urlpatterns = [
    path('', StoreListAndCategoryView.as_view(), name='store'),
    path('category/<slug:category_slug>/', StoreListAndCategoryView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', search, name="search"),
    path('submit_review/<int:product_id>', submit_review, name="submit_review")
]

