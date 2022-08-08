from django.contrib import admin
from blogging.models import Category, Post, PostAdmin, CategoryAdmin,Role

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Role)