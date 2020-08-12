from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(ParentCategory, verbose_name='親カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class PostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().select_related('category__parent').prefetch_related('tag')


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    main_text = models.TextField('本文', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)

    objects = PostManager()
