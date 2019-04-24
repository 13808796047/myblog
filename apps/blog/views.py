from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings


def home(request):  # 主页
    posts = Article.objects.all()  # 获取全部的Article对象
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应在setting.py中的PAGE_NUM
    page = request.GET.get('page')  # 获取url中的page参数值
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/home.html', {'post_list': post_list})


def detail(request, pk):  # 查看文章详情
    post = get_object_or_404(Article, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post.html', context)
    # return render(request, 'blog/post.html', locals())
    # post = get_object_or_404(Article, pk=article_id)
    # post.viewed()  # 更新浏览次数
    # tags = post.tags.all()  # 获取文章对应所有标签
    # context = {'post': post, 'tags': tags}
    # return render(request, 'post.html', context)
