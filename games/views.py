from django.shortcuts import render
from .models import GameContents

# Create your views here.
def games(request):
    content_list = GameContents.objects.order_by('-published_at')
    context = {'content_list': content_list}
    return render(request, 'pages/gamelist.html', context)