from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth import get_user_model
from chat.models import Message
from django.db.models import Q
from chat.forms import MessageForm
from django.http import HttpResponseRedirect

# Create your views here.

User = get_user_model()

def user_chat(request, username):
    user = get_object_or_404(User, username = username)
    users = User.objects.exclude(username = request.user.username)
    messages = Message.objects.filter(
        Q(form_user=user, to_user=request.user) | Q(form_user=request.user, to_user = user)
    )
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.from_user = request.user
        obj.to_user = user
        obj.save()
        return HttpResponseRedirect(reverse("chat:message", args=(username, )))
    context = {"users": users, "messages": messages, "form": form}

    return render(request, "chat.html", context)