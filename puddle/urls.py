from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
 

  #here all the view function defined are called for urls.py

urlpatterns = [
    path('', include('core.urls')),
    path('item/', include('item.urls', 'item')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
