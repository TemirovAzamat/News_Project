from django.http import JsonResponse
from rest_framework import generics
from rest_framework import permissions
from rest_framework import pagination
from rest_framework import filters

from . import models
from . import serializers
from . import permissions as perm


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class NewsCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author, news_id=self.kwargs['news_id'])


class NewsCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [perm.IsAdmin]


# class NewsStatusCreateAPIView(generics.CreateAPIView):
#     queryset = models.NewsStatus.objects.all()
#     serializer_class = serializers.NewsStatusSerializer
#     permission_classes = [perm.Author]
#
#     def get(self, request, news_id, slug):
#         news = models.News.objects.get(id=news_id)
#         author = request.user.author
#
#         if models.NewsStatus.objects.filter(author=author, news=news).exists():
#             return JsonResponse({"error": "You already added status"})
#
#         models.NewsStatus.objects.create(author=request.user, news=news)
#
#         return JsonResponse({"message": "Status added"})
