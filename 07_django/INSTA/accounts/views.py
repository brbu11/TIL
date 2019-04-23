from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from posts.forms import CommentModelForm
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm


# Create your views here.
@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        form = CustomUserCreateForm()
    return render(request, 'accounts/signup.html',
                  {
                      'form': form,
                  })


@require_http_methods(['GET', 'POST'])
def login(request):
    # 우선 로그인 되어있는지부터 확인

    if request.user.is_authenticated:
        return redirect('posts:post_list')

    # 로그인 안되어 있다면
    # 사용자가 로그인 데이터를 넘겼을 때, 버튼눌렀을 때
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # do login
            auth_login(request, form.get_user())
            messages.add_message(request, messages.SUCCESS, '하이!')
            return redirect(request.GET.get('next') or 'posts:post_list')
    # 사용자가 로그인 화면을 요청할때
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "accounts/login.html",
                  {
                      'form': form,
                  })


def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, '잘가!')
    return redirect('posts:post_list')


def user_detail(request):
    return None


@require_POST
@login_required
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    if sender != receiver:
        if receiver in sender.followings.all():
            # 있으니까 언팔
            sender.followings.remove(receiver)
        else:
            sender.followings.add(receiver)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
