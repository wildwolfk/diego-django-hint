from django.conf.urls.defaults import patterns, include, url
from views import hello
from django.contrib import admin
from autoComplete.views import getMeta, autoComplete, detail

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hint.views.home', name='home'),
    # url(r'^hint/', include('hint.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
    url(r'^hello/$', hello),
    url(r'^autoComplete/$', autoComplete),
    
    url(r'^meta/$', getMeta),
#    url(r'^/autoComplete/scripts/jquery-ui.js', templates/scripts/jquery-ui.js),
    url(r'^autoComplete/scripts/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': 'templates/autoComplete\scripts/' }),
    url(r'^detail/$', detail)
)
