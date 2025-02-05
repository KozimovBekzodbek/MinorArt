from django.contrib import admin
from common import models



@admin.register(models.Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ("company_name", )



@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name", )} 
    search_fields = ("name", "about")#qidirish bolimini ochish uchun



@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name", )} 
    search_fields = ("name", "about","title")#qidirish bolimini ochish uchun

