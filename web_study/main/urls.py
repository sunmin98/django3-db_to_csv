from django.contrib import admin
from django.urls import path
from .views import *
#from main.views import index, blog, posting

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

import member.views


urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>',posting, name="posting"),
    path('blog/new_post/', new_post),
    path('login/', member.views.login, name='login'),
    path('signup/', member.views.signup, name='signup'),
    path('logout/', member.views.logout, name='logout'),

    #path('blog/csv_post/',csv_post, name='csv_post'),

    path("blog/upload-file/", uploadFile, name="uploadFile"),
    path("blog/upload-filr/", downloadFile, name="downloadFile")
]


# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#?? https://hyundy.tistory.com/11
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

