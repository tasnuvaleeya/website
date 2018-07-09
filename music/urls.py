from django.conf.urls import url
from .views import index, detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', detail, name="detail"),
]