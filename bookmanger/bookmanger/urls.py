"""bookmanger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from book.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加index路由
    # path('index/', index),
    # path('blog/', include('blog.urls'))
    # 去除blog/ 以让子应用的urls可直接访问
    path('', include('book.urls'))
]
