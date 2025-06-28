from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mysite.views import *
from mysite.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('artikel/<int:id>/', detail_artikel, name="detail_artikel"),
    path('artikel-not-found/', not_found_artikel, name="not_found_artikel"),
    path('toko/', toko, name="toko"),
    path('kontak/', kontak, name="kontak"),

    path('dashboard/', dashboard, name='dashboard'),

    # ✅ Include URL dari aplikasi artikel
    path('dashboard/', include('artikel.urls')),

    # ✅ Authentication
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),

    # ✅ CKEditor & Media
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
