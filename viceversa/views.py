from django.shortcuts import render

def textarea(request):
    return render(request, 'textarea.html')

def reverse(request):
    return render(request, 'reverse.html')