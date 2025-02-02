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
        
        context = {
            "main": main,
            "slider": slider,
            "product": product,
        }

        return render(request, "index.html", context)




class AboutView(View):
    def get(self, request):
        main = models.Main.objects.all()
        
        context = {
            "main": main,
        }
        return render(request, "about.html", context)




class NewsView(View):
    def get(self, request):
        main = models.Main.objects.all()
        
        context = {
            "main": main,
        }
        return render(request, "news.html", context)






class NewsDetailView(View):
    def get(self, request):
        main = models.Main.objects.all()
        
        context = {
            "main": main,
        }
        return render(request, "news-detail.html", context)





class ProductsView(View):
    def get(self, request):
        main = models.Main.objects.all()
        product_list = models.Products.objects.all().order_by("-id")  # Barcha dorilarni olish
        per_page = 1  # Har bir sahifada faqat 1 ta mahsulot chiqadi
        paginator = Paginator(product_list, per_page)

        # Sahifa raqamini olish (foydalanuvchi URL'dan ?page=2 bo‘lsa)
        page_number = request.GET.get("page", 1)  # Agar page bo‘lmasa, 1-sahifa chiqadi
        products = paginator.get_page(page_number)  # Paginatsiyalangan dorilar

        context = {
            "main": main,
            "products": products,  # Paginatsiyalangan mahsulotlar
        }
        return render(request, "products.html", context)



class ProductDetailView(DetailView):
    queryset = models.Products.objects.all()
    slug_field = "slug"
    context_object_name = "object"
    template_name = "detail-page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["related_products"] = models.Products.objects.filter(is_top=True)

        return context




