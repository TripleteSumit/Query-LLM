from django.shortcuts import render
from .gen import Gen


def home(request):
    return render(request, template_name='chat.html')


def query(request):
    if request.method == 'POST':
        query = request.POST.get('query', None)
        if query is not None:
            app = Gen()
            app.input_knowledge()
            response = app.query(query)

    return render(request, template_name='chat.html', context={'response': response})
