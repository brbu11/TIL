from django import forms
from django.views.decorators.http import require_http_methods
from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
