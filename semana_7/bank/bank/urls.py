from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), # r = regex = regular expresion
    url(r'^', include('account.urls')),
)


#   ^ start of string (hahu)
#   $ end of string (rohan)
