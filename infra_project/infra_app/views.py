from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось даже с allowhost!')


def second_page(request):
    return HttpResponse('שבת שלום .А это вторая страница!')
