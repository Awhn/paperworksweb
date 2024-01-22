from django.shortcuts import render, get_object_or_404, redirect
from .models import GameContents
from .forms import CommentForm

# Create your views here.
def games(request):
    content_list = GameContents.objects.order_by('-published_at')
    context = {'content_list': content_list}
    return render(request, 'pages/gamelist.html', context)

def detail(request, content_id):
    content_list = get_object_or_404(GameContents, pk=content_id)
    context = { 'content_list': content_list}
    return render(request, 'pages/content_detail.html', context)

def comment_create(request, content_id):
    content_list = get_object_or_404(GameContents, pk=content_id)

    if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = content_list
        comment.author = request.user
        comment.save()
        return redirect(detail, content_id)
    else:
        form = CommentForm()
        context = {'content_list': content_list, 'form': form}
        return render(request, 'mysite/content_detail.html', context)