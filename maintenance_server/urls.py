from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'maintenance_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('maintenance_messages.urls')),
]
