# 관리자(admin)가 게시글(Post)에 접근할 권한을 준다.
# 게시글 게시, 삭제, 수정, 저장 등 여러 작업을 할 수 있게 해준다.
from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)