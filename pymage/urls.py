from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexTest, name='index'),
    path('seek', views.seek, name='seek'),
    path('rotate', views.rotate, name='rotate'),
    path('flip', views.flip, name='flip'),
    path('crop', views.crop, name='crop'),
    path('scale', views.scale, name='scale'),
    path('invert', views.invert, name='invert'),
    path('search', views.similar_search, name='search')


]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)