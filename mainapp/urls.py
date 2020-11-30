"""glossarik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from mainapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reg/', views.reg_s),
    path('login/', views.authorization),
    re_path(
        r'^(?P<group>\D+)/(?P<name>\D+)/(?P<FC>\D+)/(?P<num_work>\d+)/$', views.estima),
    re_path(r'^(?P<group>\D+)/(?P<name>\D+)/$', views.display),

]
