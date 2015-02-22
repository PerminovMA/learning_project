from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world!")


def get_data(request):
    return HttpResponse("Get data")