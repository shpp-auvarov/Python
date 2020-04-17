from django.http import HttpResponse


def index(request, text=""):
    if not text:
        return HttpResponse("Hello, world. You're at the locations index.")
    return HttpResponse(text)
