from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from calculator.models import ToyProduct, BlogPost

class ToyProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ToyProduct.objects.all()

    def location(self, obj):
        return reverse('toy_detail', args=[obj.slug])


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(published=True)

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ['home', 'toy_list', 'blog_list', 'privacy', 'contact']

    def location(self, obj):
        return reverse(obj)