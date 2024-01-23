from django.shortcuts import render, get_object_or_404, redirect
from .models import GameContents, Comments
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
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


@login_required(login_url='accounts:login')
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
    
@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect(detail, content_id=comment.content_list.id)