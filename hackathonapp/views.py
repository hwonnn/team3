from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models



# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)
    
class CommentDetailList(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)

#class CommentLike(APIView):
#    def comment_like(request, comment_id) :
#       comment = get_object_or_404(Comment, pk=comment_id)
#        user = request.user

#        if comment.like_users.filter(pk=user.pk).exists() :
#            comment.like_users.remove(user)
#            liked = False
#        else :
#            comment.like_users.add(user)
#            liked = True

#        context = {
#            'liked' : liked,
#            'count' : comment.like_users.count(),
#        }

#        return Response(context)

