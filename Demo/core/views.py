from django.shortcuts import render

def core(request):
    return render(request, 'core/core.html')


def new(request):
    return render(request, 'core/new.html')