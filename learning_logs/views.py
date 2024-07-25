from django.shortcuts import render

def index(request):
    """Home page for Learning_log app"""
    return render(request, 'learning_logs/index.html')
