from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'site/index.html', context)

def get_data(request):
    return HttpResponse('{"mihail": "krutoi", "andrey": "loh"}', content_type="text/plain")