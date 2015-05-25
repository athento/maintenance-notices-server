from django.conf.urls import url

from . import views

urlpatterns = [
    # get/default-domain/ -> returns html if in date.
    url(r'^get/(?P<domain>.+)/$', views.get, name='get'),

    # create/for/default-domain/ -> returns 200 if created ok
    # must provide config in body
    url(r'^create/$', views.create, name='create'),

    url(r'^', views.index, name='index'),
]
