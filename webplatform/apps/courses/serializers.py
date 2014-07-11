from rest_framework import serializers

from apps.courses.models import Chapter, Article


class ChaptersSerializer(serializers.ModelSerializer):
    
    kind = serializers.Field(source='get_kind')

    class Meta:

        model = Chapter
        fields = ('title', 'slug', 'summary', 'video', 'kind',)


class ArticlesSerializer(serializers.ModelSerializer):
    
    kind = serializers.Field(source='get_kind')
    
    class Meta:

        model = Article
        fields = ('title', 'slug' , 'summary', 'content', 'kind',)