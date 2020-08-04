from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'blog/index.html'
    queryset = Post.objects.all().select_related('category__parent')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
