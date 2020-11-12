from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("resume.urls", namespace='resume')),
    path('superuser/', include('django.contrib.auth.urls')),
    path('superuser/login', include("login.urls")),
    path('', include("blog.urls")),
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)