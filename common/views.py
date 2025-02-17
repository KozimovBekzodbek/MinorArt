from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import  messages
from common import models
import traceback
from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.core.paginator import Paginator




class HomeView(View):
    def get(self, request):
        main = models.Main.objects.all()
        slider = models.Slider.objects.all()
        product = models.Products.objects.filter(is_top=True).order_by("-id")
        news = models.News.objects.filter(is_top=True).order_by("-id")
        about = models.AboutUs.objects.all()

        context = {
            "main": main,
            "slider": slider,
            "product": product,
            "about": about,
            "news": news,
        }

        return render(request, "index.html", context)




class AboutView(View):
    def get(self, request):
        main = models.Main.objects.all()
        about = models.AboutUs.objects.all()
        
        context = {
            "main": main,
            "about": about,
        }
        return render(request, "about.html", context)




class NewsView(View):
    def get(self, request):
        main = models.Main.objects.all()
        left = models.News.objects.all().filter(side="chap")
        right = models.News.objects.all().filter(side="o'ng")
        
        context = {
            "main": main,
            "left": left,
            "right": right,
        }

        return render(request, "news.html", context)




class NewsDetailView(DetailView):
    queryset = models.News.objects.all()
    slug_field = "slug"
    context_object_name = "object"
    template_name = "news-detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()  
        
        context["product_images"] = models.NewsImage.objects.filter(product=product)

        context["related_products"] = models.News.objects.filter(is_top=True)

        return context




class ProductsView(View):
    def get(self, request):
        main = models.Main.objects.all()
        product_list = models.Products.objects.all().order_by("-id")  
        per_page = 16  
        paginator = Paginator(product_list, per_page)
        page_number = request.GET.get("page", 1)  
        products = paginator.get_page(page_number)  

        context = {
            "main": main,
            "products": products,  
        }

        return render(request, "products.html", context)




class ProductDetailView(DetailView):
    queryset = models.Products.objects.all()
    slug_field = "slug"
    context_object_name = "object"
    template_name = "detail-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()  
        
        context["product_images"] = models.ProductImage.objects.filter(product=product)

        context["main"] = models.Main.objects.all()
        context["related_products"] = models.Products.objects.filter(is_top=True)

        return context




