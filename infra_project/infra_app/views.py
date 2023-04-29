from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Даже несмотря на то, что вы не сказали про элоухост!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
