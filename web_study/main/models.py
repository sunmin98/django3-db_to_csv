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



#CSV --> DB
class Menu(models.Model):
		name = models.CharField(max_length=20)


class Category(models.Model):
		name = models.CharField(max_length=20)
		menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Product(models.Model):
		name  = models.CharField(max_length=100)
		price = models.IntegerField()
		category = models.ForeignKey('Category', on_delete=models.CASCADE)