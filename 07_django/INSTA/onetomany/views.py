from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .forms import *
from .models import Writer, Book, Chapter


# Create your views here.


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == "POST":
        form = WriterModelForm(request.POST)
        if form.is_valid():  # 데이터 저장가능?
            form.save()
            return redirect('detail')
    else:

        form = WriterModelForm()

    return render(request, 'new.html', {
        'form': form,
    })


@require_http_methods(['POST', 'GET'])
def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == "POST":
        form = WriterModelForm(request.POST, instance=writer)

        if form.is_valid():
            form.save()
            return redirect('성공')
    else:
        form = WriterModelForm(instance=writer)

    return render(request, 'new.html', {
        'form': form,
    })
