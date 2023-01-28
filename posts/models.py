from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


User = get_user_model()

class Exam(models.Model):
    FullName = models.CharField(max_length=20)
    Universitet = models.CharField(max_length=20, default="")
    Fakulte = models.CharField(max_length=20,default="")
    Ixtisas = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.FullName

class info(models.Model):
    About=models.TextField(max_length=200)

    def __str__(self) :
        return self.About
        
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    tags = TaggableManager()
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment',on_delete=models.CASCADE)
    ad_soyad = models.CharField(verbose_name='Ad Soyad',max_length=120)
    bio = models.TextField(max_length=1000,verbose_name='Bio')
    tarix = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s'%(self.post,self.ad_soyad)