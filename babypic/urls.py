from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^babypic/', include('babypic.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^t/(?P<tid>.*)/', 'babypic.app1.views.t'),
    (r'^bbs/','babypic.app1.views.bbs'),
    (r'^message/','babypic.app1.views.message'),
    #(r'^music/','babypic.app1.views.music'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'', include('django.contrib.flatpages.urls')),
)
