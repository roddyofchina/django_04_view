#coding:utf8
"""django_04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app01.views import MyView,MyhtmlView,RedUrlView,ArticleListView,ArticleDetail
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^myview/$',MyView.as_view(), name="myview"),
	url(r'^MyhtmlView/$',MyhtmlView.as_view(),name="MyhtmlView"),
	
	#第一种直接跳转
	url(r'^roddy/$',RedirectView.as_view(url="http://www.roddypy.com"),name="roddy"),
	#第二种跳转方式
	url(r'^reditest/$',RedUrlView.as_view(),name="redtest"),
	
	#ListView
	url(r'^article/$',ArticleListView.as_view(),name="article"),
	
	#DetailView
	url(r'^article_detail/(?P<pk>\d+)/$',ArticleDetail.as_view(), name="article_detail"),
]
