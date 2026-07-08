try:
    from django.db import models  # type: ignore
    from django.utils.text import slugify  # type: ignore
except Exception:  # pragma: no cover - fallback for editors/linters when Django isn't installed
    # Minimal fallback stubs so linters/IDEs don't error when Django isn't available
    from types import SimpleNamespace

    def _field(*args, **kwargs):
        return None

    class _ModelBase:
        def __init__(self, *args, **kwargs):
            pass

    models = SimpleNamespace(
        Model=_ModelBase,
        CharField=_field,
        SlugField=_field,
        DecimalField=_field,
        IntegerField=_field,
        TextField=_field,
        URLField=_field,
        BooleanField=_field,
        DateTimeField=_field,
    )

    def slugify(value):
        # simple fallback slugify for editor usage
        return "-".join(str(value).lower().split())

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
