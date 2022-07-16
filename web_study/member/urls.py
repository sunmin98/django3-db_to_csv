from django.contrib import admin
from django.urls import path
from .views import *
#from main.views import index, blog, posting

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings
import member

urlpatterns = [
    path('login/', member.views.login, name='login'),
    path('signup/', member.views.signup, name='signup'),
    path('logout/', member.views.logout, name='logout'),
]