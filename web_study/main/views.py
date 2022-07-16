# 목록(blog)페이지에 게시판 보여주자
# 입력한 게시글을 페이지에 띄워보자
#
# web_study/main/views.py
# View(blog 함수)가 Model(Post 게시글)을 가져온다.
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# View에 Model(Post 게시글) 가져오기
from .forms import UploadFileForm
from .models import Post
from . import models
from . import DB_CSV
# 회원가입, 로그인
from django.contrib.auth.models import User
from django.contrib import auth

# 다운로드
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# index.html 페이지를 부르는 index 함수

#from .forms import UploadFileForm

fileTitle = str
title = str

def index(request):
    return render(request, 'main/index.html')


# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/blog.html', {'postlist': postlist})


# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


# def csv_post(request):
#     return render(request, 'main/upload-file.html')

@login_required
##업로드##
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        form = UploadFileForm(request.POST, request.FILES)

        fileTitle = request.POST["fileTitle"]
        # 이게 파일 제목 변수로 추정되어진다~~~~~~~~~~~~

        uploadedFile = request.FILES["uploadedFile"]
        if form.is_valid(): DB_CSV.CSV_to_DB(form.cleaned_data["uploadedFile"])

        # Saving the information in the database

    documents = UploadFileForm()

    # DB_CSV.DB_to_xlsx()

    return render(request, "main/upload-file.html", context={
        "files": documents
    })


##다운로드##
def downloadFile(request):
    DB_CSV.CSV_to_DB()
    DB_CSV.DB_to_xlsx()
    # global fileTitle
    # global title
    fileTitle = 'Seoul_temp_2017.csv'

    #file_path = os.path.abspath("media/Uploaded Files/")
    file_path = os.path.abspath("")
    file_name = os.path.basename("web_study/서울_엑셀파일실험!!.xlsx")
    fs = FileSystemStorage(file_path)

    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="날씨.csv"'

    return response
