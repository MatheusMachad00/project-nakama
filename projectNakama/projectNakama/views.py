from django.shortcuts import render


def homeplage_render(request):
    return render(request, "homepage.html")
