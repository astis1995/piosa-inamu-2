# -*- coding: utf-8 -*-
#from django.urls import path
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from . import views
from django.urls import include, path

urlpatterns = [
path('<int:pk>' , views.prueba_pk, name= "perfiles_view_linear" ),
#path('<int:pk>' , views.perfiles_view_linear, "perfiles_view_linear" ),
#url('7', views.perfiles_view_linear  , name = 'perfiles_view_linear'),
url('', views.perfiles_view_matrix , name = 'perfiles_view_matrix'),
]
