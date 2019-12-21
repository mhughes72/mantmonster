from django.urls import include, path

from avatar import views

urlpatterns = [
    path('add/', views.add, name='avatar_add2'),
    path('change/', views.change, name='avatar_change'),
    path('delete/', views.delete, name='avatar_delete'),
    # path('render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/$',
    #     views.render_primary,
    #     name='avatar_render_primary'),
]

