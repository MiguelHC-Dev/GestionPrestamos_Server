from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'prestamos', views.PrestamoViewSet)
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Prestamos API')),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)