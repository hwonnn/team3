from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)

#superuser id:admin pw:0000

@admin.register(Post) # 아래 클래스를 데코레이터로 등록
class PostAdmin(admin.ModelAdmin): # PostAdmin 클래스를 정의
    list_display = ('id', 'title', 'created_at', 'author') # Post 모델의 id, title, created_at, author를 표시
    list_filter = ('created_at', 'author') # 필터 사이드바를 생성
    search_fields = ('title', 'content') # 검색 박스를 생성

@admin.register(Comment) # 아래 클래스를 데코레이터로 등록
class CommentAdmin(admin.ModelAdmin): # CommentAdmin 클래스를 정의
    list_display = ('id', 'post', 'content', 'created_at', 'author') # Comment 모델의 id, post, content, created_at, author를 표시
    list_filter = ('created_at', 'author') # 필터 사이드바를 생성
    search_fields = ('content',) # 검색 박스를 생성
