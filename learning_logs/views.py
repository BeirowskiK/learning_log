from django.shortcuts import render

from learning_logs.models import Topic


def index(request):
    """Home page for Learning_log app"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(requset, topic_id):
    """Display single topic with entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(requset, 'learning_logs/topic.html', context)
