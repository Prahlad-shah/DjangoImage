from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import AccountHomePageView
app_name = 'pymage'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', AccountHomePageView.as_view(), name='home'),
    path('grayscale', views.index, name='grayscale'),
    path('performance', views.performanceResult, name='performance'),
    path('rotate', views.rotate, name='rotate'),
    path('flip', views.flip, name='flip'),
    path('crop', views.crop, name='crop'),
    path('scale', views.scale, name='scale'),
    path('invert', views.invert, name='invert'),
    path('search', views.searchFlickrData, name='search'),
    # path('seektest', views.seekTest, name='test')


]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)