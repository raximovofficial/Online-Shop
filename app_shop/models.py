from django.db import models
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=123)
    icon = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=123, unique=True, default=timezone.now)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    slug = models.SlugField(max_length=123, default=timezone.now)
    image = models.ImageField(upload_to='images/',
                              blank=True)
    file = models.FileField(upload_to='files/',
                            blank=True)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
