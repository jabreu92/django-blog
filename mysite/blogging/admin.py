from django.contrib import admin
from blogging.models import Category, Post, PostAdmin, CategoryAdmin

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
