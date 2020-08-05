from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('category/<int:pk>', views.category_filter, name='category_filter'),
    path('tag/<int:pk>', views.tag_filter, name='tag_filter'),
]
