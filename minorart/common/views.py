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
        return render(request, "index.html")




class HomeView(View):
    def get(self, request):
        return render(request, "index.html")
