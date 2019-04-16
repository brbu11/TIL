from django import forms
from django.views.decorators.http import require_http_methods
from .models import Post, Image


class PostModelForm(forms.ModelForm):
    # content = forms.EmailField(label='Your email')
    class Meta:
        model = Post
        fields = '__all__'
        #  fields = ['content', 'image']


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        widgets = {

            'file': forms.FileInput(attrs={'multiple': True})

        }
