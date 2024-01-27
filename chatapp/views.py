from django.shortcuts import render


def query(request):
    return render(request, template_name='chat.html')
