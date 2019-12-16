from django.urls import path

from . import views
urlpatterns = [
    path('',views.category_index,name='blog_index'),
    path('blogs/',views.blog_category,name='blog_category'),
    path('<int:pk>/',views.blog_detail,name='blog_detail')
]

