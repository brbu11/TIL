from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Posting, Comment
from django.views.decorators.http import require_http_methods


# Create your views here.

# Create

@require_http_methods(['POST', 'GET'])
def create_posting(request):
    if request.method == 'GET':
        return render(request, 'board_ad/new.html')
    else:
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('title')
        posting.save()
        return redirect('board_ad:posting_detail')


# Read
def posting_list(request):
    postings = Posting.objects.all()
    # postings = get_list_or_404(Posting)
    return render(request, 'board_ad/list.html', {
        'postings': postings,
    })


def posting_detail(request, id):
    posting = get_object_or_404(Posting, id=id)
    comments = posting.comment_set.all()
    return render(request, 'board_ad/detail.html', {
        'postings': posting,
        'comments': comments,
    })


def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)

    if request.method == 'POST':
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', id=posting.id)
    else:
        return render('board_ad/update.html', {
            'posting': posting,
        })


@require_http_methods(['POST'])
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


@require_http_methods(['POST'])
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.posting = posting
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)



@require_http_methods(['POST'])
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return redirect('board_ad:posting_detail', posting_id=posting.id)