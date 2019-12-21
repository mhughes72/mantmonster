from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'publish', 'slug', 'get_theURL')
        # fields = "__all__"