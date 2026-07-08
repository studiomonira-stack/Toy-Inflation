try:
    from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
except Exception:
    admin = None
try:
    from django.urls import path # type: ignore
except Exception:
    # Provide a clear error if django.urls is unavailable (e.g., in static analysis
    # environments). This mirrors the try/except used for django.contrib.admin above.
    def path(route, view, kwargs=None, name=None):
        raise ImportError("django.urls.path is not available")
from calculator import views

urlpatterns = [
    # include admin site only if django.contrib.admin is available
    *( [path('admin/', admin.site.urls)] if admin is not None else [] ),
    path('', views.home, name='home'),
    path('leksaker/', views.toy_list, name='toy_list'),
    path('leksak/<slug:slug>/', views.toy_detail, name='toy_detail'),
    path('blogg/', views.blog_list, name='blog_list'),
    path('blogg/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('ansvar/', views.privacy, name='privacy'),
    path('setup/', views.setup_admin, name='setup_admin'),
]