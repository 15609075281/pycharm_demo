"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from . import views
from untitled.api import websocket_1

urlpatterns = [

    url(r'^py_phone$', views.phone),
    url(r'^one$', views.one),
    url(r'^two$', views.two),
    url(r'^echo$', websocket_1.echo),
    #获取平台标签
    url(r'^get_tag$', views.get_tag),
    #根据传入的标签获取所有数据
    url(r'^get_platform$', websocket_1.get_platform),

]
