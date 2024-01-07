import ckeditor.fields
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    ingredients = forms.CharField(widget=CKEditorWidget, label='')

    class Meta:
        model = Post
        exclude = ['slug', 'author', 'time_to_read']
        widgets = {
            'ingredients': ckeditor.fields.RichTextField()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Комментарий'})
        }

