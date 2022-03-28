# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from chat.models import Thread, Chat


@login_required
def index(request):
    threads = Thread.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    header = []
    for thread in threads:
        message_thread = thread.chat_thread.all()

        last_message = message_thread[0].message if message_thread.count() > 0 else "..."
        header.append(
            {
                "id": thread.id,
                "user": thread.sender if thread.sender != request.user else thread.receiver,
                "message": last_message,
            }
        )
    context = {
        "header": header,
        "chat": []
    }
    return render(request, 'chat.html', context)


@login_required
def chat_thread(request, pk):

    threads = Thread.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    print(request.user)
    header = []
    for thread in threads:
        last_message = thread.chat_thread.all().order_by("-created_at").last()
        header.append(
            {
                "id": thread.id,
                "user": thread.sender if thread.sender != request.user else thread.receiver,
                "message": last_message.message if last_message is not None else "...",
            }
        )
    user2 = Thread.objects.get(pk=pk)
    context = {
        "header": header,
        "chat": Chat.objects.filter(thread_id=pk),
        "user2": user2.sender.id if user2.sender != request.user else user2.receiver.id
    }
    return render(request, 'chat.html', context)




