from django import forms 
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", 'PreviewImage', 'author', 'category', 'status', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post title...'}),
            'PreviewImage':forms.FileInput(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-control col-sm-4'}),
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control col-sm-4'}),
            'status':forms.Select(attrs={'class': 'form-control col-sm-4'}),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...' }),
        }


class EditPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", 'PreviewImage','category', 'status', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post title...'}),
            'PreviewImage':forms.FileInput(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...' }),
        }

