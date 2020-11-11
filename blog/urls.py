from django.urls import path 
from .views import *


urlpatterns = [
    #path('blog', views.blog, name='blog'),
    path("blog/<int:pk>", ArticleDetailView.as_view(), name="article"),
    path("blog", BlogView.as_view(), name="blog"),
    path("dashboard/", DashboardCreateView.as_view(), name="dashboard"),
    
    path("dashboard/blog/add-new", AddPost.as_view(), name="add-post"),
    path("dashboard/blog/update-post", UpdatePostListView.as_view(), name="update-post-list"),
    path("dashboard/blog/add-category", AddCategory.as_view(), name="add-category"),
    path("dashboard/blog/edit-post/<int:pk>", EditPostView.as_view(), name="edit-post"),
    path("dashboard/blog/<int:pk>/delete", PostDeleteView.as_view(), name="delete-post"),
    path("blog/category/<str:cat>/", CategoryView, name="category"),
    ] 