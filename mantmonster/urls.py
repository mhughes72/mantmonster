

from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from mantmonster.sitemaps import PostSitemap
from posts import views as blog_views
from users.models import CustomUser as User
from rest_framework import routers, serializers, viewsets

#REST INCLUDES
from django.conf.urls import url
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('posts/<int:id>/', blog_views.post_list, name='post'),
    path('', include(('pages.urls', 'pages'), namespace='pages')),
    path('avatar/', include(('avatar.urls', 'avatar'), namespace='avatar')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('scraper/', include(('scraper.urls', 'scraper'), namespace='scraper')),
    # path('scraper/', TemplateView.as_view(template_name="pysics_list.html")),
    path('postsREST/', blog_views.PostList.as_view()),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG is True:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

