from django.shortcuts import render


def index(request):
    context = {
        'text': 'Real-Time Integers'
    }

    return render(request, 'index.html', context)
