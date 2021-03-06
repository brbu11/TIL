from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post, Image, HashTag
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@login_required()
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        post_form = PostModelForm(request.POST, request.FILES)
        # Data 검증을 한다.
        if post_form.is_valid():
            # 통과하면 저장한다.
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            # create Hash Tag => <input name='tags' /> #hi #ssafy #20층
            content = post_form.cleaned_data.get('content')
            words = content.split(' ')  # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)
                    post.tags.add(tag[0])
                    if tag[1]:
                        messages.add_message(request, messages.SUCCESS, f'#{tag[0].content}를 처음으로 추가하셨어요!')

            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()

            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
    # GET 방식으로 요청이 오면,
    else:
        post_form = PostModelForm()
    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        if request.method == "POST":
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                # update hashtag
                post.tags.clear()  # 기존의 태그 다날리기

                content = post_form.cleaned_data.get('content')
                words = content.split(' ')  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)
                        post.tags.add(tag[0])
                        if tag[1]:
                            messages.add_message(request, messages.SUCCESS, f'#{tag[0].content}를 처음으로 추가하셨어요!')

                return redirect('posts:post_list')

        else:
            post_form = PostModelForm(instance=post)

    else:
        return redirect('posts:post_list')

    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


@require_http_methods(['GET'])
def post_list(request):
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        comment_form = CommentModelForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # Todo
    else:
        comment_form = CommentModelForm()
    return render


@login_required
@require_http_methods(['POST'])
def toggle_likes(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:post_list')


@require_http_methods(['GET'])
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html',
                  {
                      'posts': posts,
                      'comment_form': comment_form,
                  })
