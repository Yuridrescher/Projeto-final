from django.contrib import admin
from django.urls import path
from .settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from cardapio.views import lanche, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:slug>/', lanche),
    path('', index),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
