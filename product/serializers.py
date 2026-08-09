
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'price', 'description', 'cover_image', 'cover_image_url']
    
    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None
    