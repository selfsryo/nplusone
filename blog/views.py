from django.views import generic
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post, Category, Tag


def index(request):
	context = {
		'posts': Post.objects.all(),
		'tags': Tag.objects.all(),
	}
	return render(request, 'blog/index.html', context)


def detail(request, pk):
	return render(request, 'blog/detail.html', {'post': get_object_or_404(Post, pk=pk)})


def category_filter(request, pk):
	return render(request, 'blog/category_filter.html', {'category': get_object_or_404(Category, pk=pk)})


def tag_filter(request, pk):
	return render(request, 'blog/tag_filter.html', {'tag': get_object_or_404(Tag, pk=pk)})




