from django.contrib.sitemaps import Sitemap
from posts.models import Post
# from blog.models import Entry

class PostSitemap(Sitemap):

    def items(self):
        print('SITEMAP')
        print(Post.objects.all())
        changefreq = "never"
        priority = 0.5
        # return Post.objects.all()

        return Post.objects.filter(draft=False)




