from django.contrib import admin

from .models import Post, Category, ParentCategory


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'parent')


class ParentCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ParentCategory, ParentCategoryAdmin)
