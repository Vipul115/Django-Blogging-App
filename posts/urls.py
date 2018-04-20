from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import post_detail,post_update,post_list,post_delete,post_create
urlpatterns = [
    url(r'^$', post_list),
    url(r"^(?P<id>\d+)", post_detail),
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete)

]