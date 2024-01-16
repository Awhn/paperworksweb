from django.shortcuts import render, get_object_or_404
from .models import GameContents

# Create your views here.
def games(request):
    content_list = GameContents.objects.order_by('-published_at')
    context = {'content_list': content_list}
    return render(request, 'pages/gamelist.html', context)

def detail(request, content_id):
    content_list = get_object_or_404(GameContents, pk=content_id)
    context = { 'content_list': content_list}
    return render(request, 'pages/content_detail.html', context)