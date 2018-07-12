from django.conf.urls import url
# from .views import index, detail
from .views import AlbumDeatilView, IndexView, AlbumCreateView, AlbumDeleteView, AlbumUpdateView
app_name = 'music'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', AlbumDeatilView.as_view(), name="detail"),
    # url(r'^?P<album_id>[0-9]+/favourite/',favourite, name='favourite'),
    url(r'^album/add/$', AlbumCreateView.as_view(), name='album-add'),
    url(r'^album/(?P<pk>[0-9]+)/$', AlbumUpdateView.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDeleteView.as_view(), name='album-delete'),
]