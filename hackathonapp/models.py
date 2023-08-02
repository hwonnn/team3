from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성 시간
    image = models.ImageField(upload_to='images/', blank=True, null=True) # 이미지 필드 추가
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True) # User 모델과 연결

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Post 모델과 연결
    content = models.TextField(default="빈 댓글입니다.")
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성 시간
    image = models.ImageField(upload_to='images/', blank=True, null=True) # 이미지 필드 추가
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True) # User 모델과 연결

    def __str__(self):
        return f"{self.post.title} - {self.content}"
