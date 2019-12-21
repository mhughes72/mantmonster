from django.contrib import admin
from django.conf import settings

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):

	prepopulated_fields = {"slug": ("title", "publish")}
	list_display = ["title", "updated", "publish"]
	list_display_links = ["updated"]
	list_editable = ["title", "publish"]
	list_filter = ["updated", "timestamp", "publish"]

	search_fields = ["title", "content", "publish"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)