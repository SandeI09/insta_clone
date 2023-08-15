from django.shortcuts import render, reverse, get_object_or_404
from post.models import Post
from post.forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_feed(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts" : posts}

    return render(request, "home_feed.html", context)

@login_required
def add_post(request):
    # form = TestForm(request.POST or None)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # context = {"form": form}

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj = form.save(commit=False)   # Gives the object of the post
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form" : form}

    return render(request, "add_post.html", context)


@login_required
def edit_post(request, post_id):

    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     raise Http404("Such page doesn't exist!")

    post =get_object_or_404(Post, id=post_id, user=request.user)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form": form}

    return render(request, "edit_post.html", context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(post, id = post_id,user = request.user)
    post.delete()
    return HttpResponseRedirect(reverse("post:home"))
