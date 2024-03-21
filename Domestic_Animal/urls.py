"""
URL configuration for Domestic_Animal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    # Uncomment the URL patterns you want to use
    # path('', views.animal),
    # path('Home/', views.Home, name='home'), 
    # path('blogs/', views.blogs, name='blogs'),
    # path('farm/', views.farm, name='farm'),
    # path('hospital/', views.hospital, name='hospital'),
    # path('login/', views.login, name='login'),
    # path('seller/', views.seller, name='seller'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)