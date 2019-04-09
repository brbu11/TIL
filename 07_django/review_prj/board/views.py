from django.shortcuts import render, redirect
from .models import Article


# Create your views here.


def article_new(request):
    return render(request, 'board/new.html')


def article_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })


def article_edit(request, id):
    article = Article.objects.get(id=id)

    return render(request, 'board/edit.html', {
        'article': article,
    })


def article_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/{article.id}')


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/board_ad/articles/')
