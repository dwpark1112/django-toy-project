from django.conf.urls import url
from blog.views import *

urlpatterns = [
    # example: /
    url(r'^$', PostLV.as_view(), name='index'),

    # example: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostMAV.as_view(), name='post_month_archive'),

    # example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # example: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    # example: /tag/tagName/
    url(r'tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    # example: /search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # example: /add/
    url(r'^add/$', PostCreateView.as_view(), name="add"),

    # example: /change/
    url(r'^change/$', PostChangeLV.as_view(), name="change"),

    # example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update"),

    # example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete"),
]
