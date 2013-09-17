from django.conf.urls import patterns, include, url
from bookinfo import views
from book import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^search/$', views.search),
    #(r'^showsome/(?P<searchfor>\w+)/$',views.showsome),
    #url(r'^$',home),
    # url(r'^bookinfo/', include('bookinfo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
