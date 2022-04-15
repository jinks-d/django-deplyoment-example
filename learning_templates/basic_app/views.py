from django.shortcuts import render


def index(request):
    index_context = {
        'text': "hello world",
        'number': 100
    }
    return render(request, 'basic_app/index.html', context=index_context)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
