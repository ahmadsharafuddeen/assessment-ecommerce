from django.urls import path
from .views  import StoreListAndCategoryView


app_name = "store"
urlpatterns = [
    path('', StoreListAndCategoryView.as_view(), name='store'),
    # path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    # path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    # path('search/', views.search, name="search"),
]

