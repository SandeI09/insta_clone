from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from chat.models import Message
from django.db.models import Q

# Create your views here.

User = get_user_model()

def user_chat(request, username):
    user = get_object_or_404(User, username = username)
    users = User.objects.exclude(username = request.user.username)
    messages = Message.objects.filter(
        Q(form_user=user, to_user=request.user) | Q(form_user=request.user, to_user = user)
    )
    context = {"users": users, "messages": messages}

    return render(request, "chat.html", context)