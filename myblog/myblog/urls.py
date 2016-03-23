"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(r'^list/$', 'blog.views.list'),
    url(r'^artical/(?P<aid>\d+)/$', 'blog.views.artical'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^addblog/$', 'blog.views.addblog'),
    url(r'^addtag/$', 'blog.views.addtag'),
    url(r'^addblogok/$', 'blog.views.addblogok'),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/$','blog.views.archive_month'),
    url(r'^tag/(?P<tag>\w+)/$', 'blog.views.tagDetail'),
    url(r'^missyou/$', 'blog.views.missyou'),

]
