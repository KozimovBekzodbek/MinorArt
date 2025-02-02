from django.contrib import admin
from common import models



@admin.register(models.Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ("company_name", )



@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", )
