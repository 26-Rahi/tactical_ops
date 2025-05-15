from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/confirm_delete.html', {'post': post})
    

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
         

# Create your views here.
