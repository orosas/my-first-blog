from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(error_messages = {'required': 'Campo Title Requerido'})

    class Meta:
        model = Post
        fields = ('title', 'text')
