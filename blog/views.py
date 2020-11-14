from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category 
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy


##################################################BlogViews################################################
#This view will show all the blogs we have published.
class BlogView(ListView): 
    queryset = Post.published.all()
    model = Post
    template_name = "blog/blog.html"
    ordering = ['-publish_date']

#This view will show all our posts within a certain category
def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))

    context= {'cat':cat.title().replace('-', ' '), 'category_posts': category_posts}

    return render(request, 'blog/categories.html', context)

#This will be the article view where we can read a full blog post.
class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_detail.html"

#This is where we will have our portfolio edit 
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

def listcategory(request):
    cat_list = Category.objects.all()

    context = {'cat_list':cat_list}

    return render(request, "blog/add-category.html", context)


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog/edit-post.html"
    #fields = ['title', 'preview_image', 'body']

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


def thedashboard(request):
    post_count = Post.objects.all().count()

    context={'post_count':post_count, }
    return render(request, "blog/dashboard.html", context)






