from django.urls import path
from common import views

app_name = "common"

urlpatterns = [
        path("", views.HomeView.as_view(), name="home"),
        path("about/", views.AboutView.as_view(), name="about-us"),
        path("news/", views.NewsView.as_view(), name="news"),
        path("news-detail/", views.NewsDetailView.as_view(), name="news-detail"),
        path("products/", views.ProductsView.as_view(), name="products"),
        path("product-detail/", views.ProductDetailView.as_view(), name="product-detail"),
       ]

