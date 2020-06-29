from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PostCreationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from .models import Post, Comment

# Create your views here.


# def index(request):
#     posts = Post.objects.all()[:5]
#     context = {
#         'title': "Home",
#         'posts': posts
#     }
#     return render(request, 'blog/index.html', context)

class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    queryset = Post.objects.order_by('-id').all()
    paginate_by = 3
    context_object_name = 'posts'


def signup(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account has been created successfully, You can now login.')
            return redirect('blog:login')
    else:
        form = UserRegistrationForm()

    context = {
        'title': "Register",
        'form': form
    }
    return render(request, 'blog/signup.html', context)


@login_required
def createPost(request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.published = 'published'
            obj.save()
            messages.success(request, 'Your Post is now live')
            return redirect('blog:home')

    context = {'form': form}

    return render(request, 'blog/create.html', context)


def post_details(request, title):
    post = Post.objects.get(title=title)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    context = {
        'comments': comments,
        'form': form,
        'post': post, 'title': 'Create A Post'
    }
    return render(request, 'blog/details.html', context)


@login_required
def myposts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts}
    return render(request, 'blog/myposts.html', context)


@login_required
def add_comment(request, id):
    form = CommentForm()
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by('-id').all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = post

            obj.save()
            messages.success(request, 'Comment Added Successfully')
            return redirect(f'/comment/{post.id}')

    context = {
        'form': form,
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/comment.html', context)


@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)

    if request.method == 'POST':
        comment.delete()
        return redirect(f'/comment/{comment.post.id}')

    context = {
        'comment': comment,

    }
    return render(request, 'blog/delete_comment.html', context)


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully')
        return redirect('blog:home')

    context = {
        'post': post,

    }
    return render(request, 'blog/delete_post.html', context)
