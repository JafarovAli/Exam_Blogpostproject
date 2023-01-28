from django.shortcuts import render,get_object_or_404
from django.db.models import Q 
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from taggit.models import Tag
from .forms import CommentForm
from .models import Category, Post, Author,Exam,info


def exam (request):
    name=Exam.objects.get()

    Context = {
        'name': name,
    }
    return render(request,'Exam.html',Context)

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None
    
def postlistauthor (request,author_id):
    posts = Post.objects.filter(author_id=author_id).order_by('-timestamp')
    author = Author.objects.get(user_id = author_id)

    context = {
        'posts': posts,
        'author' : author,

    }
    return render(request, 'postlist_author.html', context)
    

def homepage (request):
    categories = Category.objects.all()[0:5]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html',context)



    
def post (request,slug):
    try:
        post = Post.objects.get(slug=slug)
        latest = Post.objects.order_by('-timestamp')
    except ObjectDoesNotExist:
        raise Http404    

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        comment_form = CommentForm()
    context = {
        'post': post,
        'latest': latest,
        'form':comment_form,
    }
    return render(request, 'post.html', context)


def about (request):
    melumat=info.objects.get()
    context = {
        'melumat' :melumat
    }
    return render(request, 'about_page.html',context)
    


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'search_bar.html', context)

def postlist (request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)   

def allposts(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)



def post_list(request, tag_slug=None):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    context = {
        'posts': posts,
        'tag': tag
    }
    return render(request, 'post_list.html',context)

