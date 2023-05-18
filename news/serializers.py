from rest_framework import serializers

from . import models


class NewsSerializer(serializers.ModelSerializer):
    get_status = serializers.ReadOnlyField()

    class Meta:
        model = models.News
        fields = '__all__'
        read_only_fields = ['author', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['author', 'news']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class NewsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsStatus
        fields = '__all__'


