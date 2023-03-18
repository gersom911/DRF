from rest_framework.serializers import ModelSerializer
from nueva.models  import post
from rest_framework import serializers

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = post
        #campo que devolverá 
        fields =('id', 'title', 'content','text')
