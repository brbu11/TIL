from django.shortcuts import render, redirect
from .models import Posting


# Create your views here.

def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings ,
    })

def posting_detail(request, id):
    posting = Posting.objects.get(id=id)
    return render(request, 'board_ad/detail.html', {
        'postings': posting ,
    })
