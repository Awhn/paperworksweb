from django.urls import path
from . import views

urlpatterns = [
    path('', views.games),
    path('<int:content_id>/', views.detail),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update,name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]