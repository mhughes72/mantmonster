from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path




from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)



urlpatterns = [
	path('', post_list, name='list'),
    path('create/', post_create),
    path('<slug>/', post_detail, name='detail'),
    path('<slug>/edit/', post_update, name='update'),
	# path    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

