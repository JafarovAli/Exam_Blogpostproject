from django.contrib import admin

from .models import Author, Category, Post,Exam,info,Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Exam)
admin.site.register(info)
admin.site.register(Comment)
