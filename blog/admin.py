from django.contrib import admin

from .models import Post, Category, ParentCategory, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ParentCategory, ParentCategoryAdmin)
admin.site.register(Tag, TagAdmin)
