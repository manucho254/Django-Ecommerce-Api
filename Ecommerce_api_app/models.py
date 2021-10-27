from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models  import User

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        ordering = ("category_name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Product(models.Model):
    product_vendor  = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    product_thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    product_category = models.ForeignKey(Category,  related_name="categories", on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return '{}-{}'.format(self.product_category, self.product_name)

    def get_absolute_url(self):
        return f'/{self.product_category.slug}/{self.slug}/'

    def get_product_image(self):
        if self.product_image:
            return 'http://127.0.0.1:8000' + self.product_image.url
        return ''
    
    def get_product_thumbnail(self):
        if self.product_thumbnail:
            return 'http://127.0.0.1:8000' + self.product_thumbnail.url
        else:
            if self.product_image:
                self.product_thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.product_thumbnail.url
            else:
                return ''

    def make_thumbnail(self, product_image, size=(300, 200)):
        img = Image.open(product_image)
        img.convert('RGB')
        img.product_thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=product_image.product_name)

        return thumbnail

    
