from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from calculator.models import ToyProduct, BlogPost

class ToyProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ToyProduct.objects.all().order_by('name')

    def location(self, obj):
        return reverse('toy_detail', args=[obj.slug])


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(published=True).order_by('-created_at')

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])