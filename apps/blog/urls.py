from django.urls import path, include
from . import views
app_name='blog'
urlpatterns = [
    path('<int:pk>', views.detail, name='article_detail'),
]
