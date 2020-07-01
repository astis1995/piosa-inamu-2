# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from . import views

admin.autodiscover()
#app_name = "mysite"

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    #url(r'^polls/', include('polls.urls', namespace="polls")), #se quita por el apphook
    #url('en/', include('busqueda.urls')),
    url(r'^busqueda/', include('busqueda.urls')),
    #url(r'', views.home_view, name = 'home' ),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
