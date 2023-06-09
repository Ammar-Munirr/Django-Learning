"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views as ap1
from app2 import views as ap2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include([
        path('home/',ap1.home,name='home'),
        path('hello/',ap1.hello,name='hello'),
        path('template/',ap1.tempelate,name='template')
    ])),
    path('app2/',include([
        path('home/',ap2.home,name='hm'),
        path('hello/',ap2.hello),
        path('template/',ap2.template)
    ]))
]
