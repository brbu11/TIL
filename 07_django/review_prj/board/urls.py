from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('index/', views.index),
    path('greeting/<str:name>/<str:role>', views.greeting),

    path('articles/new/', views.article_new),
    path('articles/create/', views.article_create),
    path('articles/', views.article_list),
    path('articles/<ind:id>/', views.article_detail),
    path('articles/<ind:id>/edit/', views.article_edit),
    path('articles/<ind:id>/update/', views.article_update),
    path('articles/<ind:id>/delete/', views.article_delete),

]
