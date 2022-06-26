"""Vizid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from display import views as dis_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dis_view.home,name="index"),
    path('section/', dis_view.SectionView.as_view(),name="section"),
    path('section/<pk>', dis_view.SectionDetails.as_view(),name="sub_section"),
    path('about/', dis_view.about,name="about"),
    path('contact/', dis_view.contact,name="contact"),

]

if settings.DEBUG==False:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



