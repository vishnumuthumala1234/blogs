from django.urls import path
from .views import blog_list, create_blog,blog_detail

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', create_blog, name='create_blog'),
     path('blog/<int:post_id>/', blog_detail, name='blog_detail'),

]
