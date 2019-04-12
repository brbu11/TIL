from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    # Create
    path('new/', views.create_posting, name='create_posting'),
    # Read
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('<int:posting_id>/edit/', views.posting_update, name='posting_update'),
    path('<int:posting_id>/delete/', views.posting_delete, name='posting_delete'),
    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:posting_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

]
