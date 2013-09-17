from django.conf.urls.defaults import *
from views import search

urlpatterns = patterns('',
        (r'^/search/$',search),
        
)
