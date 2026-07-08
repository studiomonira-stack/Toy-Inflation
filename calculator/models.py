from django.db import models
from django.utils.text import slugify

class ToyProduct(models.Model):
    """Alla nostalgiprylar som går att räkna på"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price_year = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)  # t.ex. "Spelkonsol", "Docka"
    image_url = models.URLField(blank=True)  # för senare
    popular = models.BooleanField(default=False)  # visa på startsidan

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.original_price_year})"


class BlogPost(models.Model):
    """Nostalgiska blogginlägg - skrivs via admin"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image_url = models.URLField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
