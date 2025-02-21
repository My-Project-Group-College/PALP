from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, Message

def new_conversation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        conversation = Conversation.objects.create(
            user=request.user,
            title=title
        )
        return redirect('conversation_detail', conversation.id)
    return render(request, 'new_conversation.html')

def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    
    if request.method == 'POST':
        user_message = request.POST.get('message')
        Message.objects.create(
            conversation=conversation,
            content=user_message,
            is_user=True
        )
        # Add AI response logic here (e.g., call an API or generate a response)
        ai_response = "This is a sample AI response."
        Message.objects.create(
            conversation=conversation,
            content=ai_response,
            is_user=False
        )
        return redirect('conversation_detail', conversation.id)
    
    return render(request, 'conversation_detail.html', {
        'conversation': conversation,
        'messages': messages
    })