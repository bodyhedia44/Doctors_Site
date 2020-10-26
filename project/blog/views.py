from django.shortcuts import render, redirect,reverse
from .models import Post
from django.shortcuts import get_object_or_404 
from jobs.forms import AddComment
from accounts.models import Comment
from .filter import BFilter
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.


def blog(request):
    post=Post.objects.all().order_by("-time")
    old=Post.objects.all()[:2]
    myfilter=BFilter(request.GET,queryset=post)
    post=myfilter.qs
    paginator = Paginator(post, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home2.html',{"posts":page_obj,"old":old,"myfilter":myfilter})


def single(request,slug):
    post=get_object_or_404(Post,title=slug)
    old=Post.objects.all()[:2]
    w=str(request)
    where=w.split("'")
    comms=Comment.objects.filter(where=where[1])
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.name=str(request.user)
            myform.comment=form.cleaned_data['comment']
            myform.where=where[1]
            myform.save()
            form=AddComment()
            return redirect("/blog")
    else:
        form=AddComment()
    return render(request,'single.html',{"post":post,"form":form,"comms":comms,"old":old})



def like_unlike(request,slug):
    post=get_object_or_404(Post,title=slug)
    if request.user in post.like.all():
        post.like.remove(request.user)
    
    else:
        post.like.add(request.user)
    return HttpResponse()
    
