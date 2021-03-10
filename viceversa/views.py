from django.shortcuts import render

def textarea(request):
    return render(request, 'textarea.html')

def reverse(request):
    user_text = request.GET['text']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text})