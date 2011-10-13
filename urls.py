from django.conf.urls.defaults import patterns, include, url
from views import hello, autoComplete
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
    # url(r'^admin/', include(admin.site.urls)),
    
    url('^hello/$', hello),
    url('^autoComplete/$', autoComplete),
)
