"""config URL Configuration

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
from django.contrib import admin
from django.urls import path
from mt import views as mtview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mtview.home, name='home'),
    path('krmt/', mtview.krmt, name='krmt'),
    path('krmt/detail/<int:mt_num>/', mtview.krmt_detail, name='detail'),
    path('krmt/detailview/<int:mt_num>/', mtview.krmt_detail_view, name='detailview'),
    path('krmt/search/', mtview.search, name='search'),
    path('krmt/search/detailview/<int:mt_num>/',mtview.krmt_detail_view),
    path('krmt/search/detail/<int:mt_num>/',mtview.krmt_detail),

    path('house/', mtview.house, name='house'),
    
]
