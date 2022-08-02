from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다

class Post(models.Model):   #models.Model --> 서브 클래스
    postname = models.CharField(max_length=50)
    #postname이라느 필드는 문자열 타입이다!
    #max_length--> 필드값의 최대 길이는 50자
    mainphoto = models.FileField(blank=True, null= True)
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):  #--> 메소드   문자열을 반환하도록함
        return self.postname

#파일 업로드
class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField()



#DB 프린트
class db_print_model(models.Model):
    file_name = models.CharField(max_length=300)
    class_name = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __db_print_model_see__(self):
        return self.file_name , self.class_name , self.percent

class log_file(models.Model):
    file_name = models.CharField(max_length=300)
    class_name = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __db_print_model_see__(self):
        return self.file_name , self.class_name , self.percent