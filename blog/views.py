from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def allblog(request):
    allblogs = Blog.objects
    return render(request,'blog/allblog.html',{'allblogs':allblogs})

def detail(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detailblog.html',{'detailblog':detailblog})
