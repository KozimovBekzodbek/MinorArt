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
    slug = models.SlugField(_("slug-name"), max_length=256)
    description = models.TextField(_("description"))
    main_image = ResizedImageField(_("asosiy rasm"),  quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    image_1 = ResizedImageField(_("rasm - 1"), blank=True, null=True , quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    image_2 = ResizedImageField(_("rasm - 2"), blank=True, null=True , quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    image_3 = ResizedImageField(_("rasm - 3"), blank=True, null=True ,quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    image_4 = ResizedImageField(_("rasm - 4") ,blank=True, null=True , quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    image_5 = ResizedImageField(_("rasm - 5"), blank=True, null=True ,quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    is_top = models.BooleanField(_("project is top"), default=False)
    date = models.DateField(_("date"), default=timezone.now)
    content = RichTextField(_("qo'llanishi va qo'shimcha ma'lumotlar"))



