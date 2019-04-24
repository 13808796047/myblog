from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings

categories = Category.objects.all()  # 获取全部的分类对象
tags = Tag.objects.all()  # 获取全部的标签对象


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
    return render(request, 'blog/home.html', {'post_list': post_list, 'category_list': categories})


def detail(request, pk):  # 查看文章详情
    post = get_object_or_404(Article, pk=pk)
    post.viewed()  # 更新浏览次数
    tags = post.tags.all()  # 获取文章对应所有标签
    return render(request, 'blog/post.html', {'post': post, 'tags': tags,'category_list': categories})


def search_category(request, pk):  # 分类搜索
    posts = Article.objects.filter(category_id=pk)
    category = get_object_or_404(Category, pk=pk)
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html',{'post_list': post_list, 'category_list': categories, 'category': category})


def search_tag(request, tag):  # 标签搜索
    posts = Article.objects.filter(tags__name__contains=tag)

    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量
    try:
        page = request.GET.get('page')  # 获取URL中page参数的值
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/tag.html', {'post_list': post_list, 'category_list': categories, 'tag': tag})
