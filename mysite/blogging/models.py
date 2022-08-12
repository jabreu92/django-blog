# Create your models here.
from django.db import models  # <-- This is already in the file
from django.contrib.auth.models import User
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
