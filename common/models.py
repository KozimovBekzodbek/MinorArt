from django.db import models
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField




class Main(models.Model):
    icon =models.FileField(_("vebsite iconkasi"),   upload_to="icon/%Y/%m")
    logo = models.FileField(_("Logotip bu navbardagisi"),   upload_to="logo/%Y/%m")
    logo_footer = models.FileField(_("Logotip bu footerdagisi"),  upload_to="logo/%Y/%m")
    company_name = models.TextField(_("Kompaniya to'liq nomi"))
    location = models.TextField(_("Manzil"))
    telegram = models.CharField(_("telegram url"), max_length=256)
    instagram = models.CharField(_("instagram url"), max_length=256)
    facebook  = models.CharField(_("facebook url"), max_length=256)
    youtube  = models.CharField(_("youtube url"), max_length=256)
    linkedin = models.CharField(_("linkedin url"), max_length=256)

    class Meta:
        db_table = "Asosiy"
        verbose_name = _("Asosiy")
        verbose_name_plural = _("Asosiy kompanentlar")

    def __str__(self):
        return f"{self.company_name}"




class Slider(models.Model):
    image =models.FileField(_("header slider"),upload_to="icon/%Y/%m")
    title = models.CharField(_("Sarlavha"), max_length = 256)
    about = models.TextField(_("Haqida"))

    class Meta:
        db_table = "Slider"
        verbose_name = _("Slider")
        verbose_name_plural = _("Header Slider")

    def __str__(self):
        return f"{self.title}"




class Products(models.Model):
    name = models.CharField(_("Mahsulot nomi"), max_length=256)
    about = models.CharField(_("Mahsulot haqida"), max_length=256)
    slug = models.SlugField(_("url-name"),unique=True, max_length=256)
    description = models.TextField(_("description"))
    main_image = ResizedImageField(_("asosiy rasm"),  quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    is_top = models.BooleanField(_("Asosiy pageda tursinmi"), default=False)
    date = models.DateField(_("date"), default=timezone.now)
    content = models.TextField(_("qo'llanishi va qo'shimcha ma'lumotlar"))

    class Meta:
        db_table = "Mahsulot"
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")

    def __str__(self):
        return f"{self.name}"




class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(_("mahsulot uchun qo'shimcha rasmlar"),upload_to="products/%Y/%m/")  

    class Meta:
        db_table = "Mahsulot rasmlar"
        verbose_name = _("Mahsulot rasmlar")
        verbose_name_plural = _("Mahsulotlar rasmlar")

    def __str__(self):
        return f"Image for {self.product.name}"




class AboutUs(models.Model):
    title = models.CharField(_("Sarlavha"),max_length=256)
    main_description = models.TextField(_("asosiy page uchun ma'lumot"))
    description = models.TextField(_("Biz haqimizda page uchun ma'lumot"))
    small_image = models.FileField(_("asosiy page uchun rasm"))
    large_image = models.FileField(_("Biz haqimizda page uchun rasm"))

    class Meta:
        db_table = "BizHaqimizda"
        verbose_name = _("BizHaqimizda")
        verbose_name_plural = _("BizHaqimizda")

    def __str__(self):
        return f"{self.title}"




class YesNo(models.TextChoices):
    Yes = "o'ng", ("o'ng")
    No = "chap", ("chap")




class News(models.Model):
    name = models.CharField(_("Mahsulot nomi"), max_length=256)
    about = models.CharField(_("Mahsulot haqida"), max_length=256)
    slug = models.SlugField(_("url-name"),unique=True, max_length=256)
    side = models.CharField(_("qaysi tomonda tursin"),max_length=256,choices=YesNo.choices)
    description = models.TextField(_("description"))
    main_image = ResizedImageField(_("asosiy rasm"),  quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    is_top = models.BooleanField(_("Asosiy pageda tursinmi"), default=False)
    date = models.DateField(_("date"), default=timezone.now)
    content = models.TextField(_("qo'llanishi va qo'shimcha ma'lumotlar"))

    class Meta:
        db_table = "Yangiliklar"
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")

    def __str__(self):
        return f"{self.name}"




class NewsImage(models.Model):
    product = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(_("yangi mahsulot uchun qo'shimcha rasmlar"),upload_to="newss/%Y/%m/")  

    class Meta:
        db_table = "Yangi mahsulot rasmlari"
        verbose_name = _("Yangi mahsulot rasmlari")
        verbose_name_plural = _("Yangi mahsulot rasmlari")

    def __str__(self):
        return f"Image for {self.product.name}"


