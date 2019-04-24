from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),  # 主页
    path('article/<int:pk>', views.detail, name='article_detail'),  # 文章详情
    path('category/<int:pk>', views.search_category, name='search_category'),  # 分类搜索
    path('tag/<str:tag>', views.search_tag, name='search_tag'),  # 标签搜索
]
