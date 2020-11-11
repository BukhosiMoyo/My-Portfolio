from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category 
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy

#def blog(request):

#    context={}
#    return render(request, 'blog/blog.html', context)

class BlogView(ListView): 
    queryset = Post.published.all()
    model = Post
    template_name = "blog/blog.html"
    ordering = ['-publish_date']

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))

    context= {'cat':cat.title().replace('-', ' '), 'category_posts': category_posts}

    return render(request, 'blog/categories.html', context)


class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_detail.html"

class DashboardCreateView(ListView):
    model = Post
    fields = '__all__'
    template_name = "blog/dashboard.html"

class PortfolioEdit(CreateView):
    model = Post
    fields = '__all__'
    template_name = "blog/portfolio-edit.html"

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    #fields = '__all__'
    template_name = "blog/add-new.html"

#Add new category to list
class AddCategory(CreateView):
    model = Category
    #form_class = PostForm
    fields = '__all__'
    template_name = "blog/add-category.html"


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog/edit-post.html"
    #fields = ['title', 'PreviewImage', 'body']

class UpdatePostListView(ListView):
    model = Post
    template_name = "blog/update-post.html"
    fields = '__all__'


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete-post.html"
    success_url = reverse_lazy('update-post-list')


# Include Views Test
class PreviewDetailView(DetailView):
    model = Post
    template_name = "blog/preview.html"







