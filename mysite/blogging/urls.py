from django.urls import path
from blogging.views import list_view
from blogging.views import detail_view
from blogging.views import BloggingListView
from blogging.views import BloggingDetailView

urlpatterns = [
    path("", BloggingListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BloggingDetailView.as_view(), name="blog_detail"),
]
