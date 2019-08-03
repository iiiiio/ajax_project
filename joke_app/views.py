from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request=request, template_name="joke_app/index.html")


def return_punchline(request):
    data = {
        'punchline': 'On a honeymoon.'
    }
    return JsonResponse(data)
