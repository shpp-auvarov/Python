from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the locations index.")


def index_second(request, text=""):
    return HttpResponse(text)

