from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
   image = serializers.ImageField(max_length=None, use_url=True)
   # image_url = serializers.SerializerMethodField()
   
   # def get_image_url(self, obj):
   #      request = self.context.get('request')
   #      if obj.image:
   #          return request.build_absolute_uri(obj.image.url)
   #      return None
     
   class Meta:
        model = Blog
        fields = '__all__'
