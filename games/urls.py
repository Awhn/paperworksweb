from django.urls import path
from . import views
urlpatterns = [
    path('', views.games),
    path('<int:content_id>/', views.detail)
]