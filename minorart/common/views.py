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




class HomeView(View):
    def get(self, request):
        main = models.Main.objects.all()
        slider = models.Slider.objects.all()
        
        context = {
            "main": main,
            "slider": slider,
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
        
        context = {
            "main": main,
        }
        return render(request, 'products.html', context)

class ProductDetailView(View):
    def get(self, request):
        main = models.Main.objects.all()
        
        context = {
            "main": main,
        }
        return render(request, 'detail-page.html', context)


