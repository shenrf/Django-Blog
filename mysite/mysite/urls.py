"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
=======
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
>>>>>>> d77f5829752f031379513206e62b4778083c0009
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD

urlpatterns = [
    url(r'^admin/', admin.site.urls),
=======
from blog.views import process_index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^content/$', process_index),
>>>>>>> d77f5829752f031379513206e62b4778083c0009
]
