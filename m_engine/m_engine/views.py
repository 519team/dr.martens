from django.http import HttpResponse

def mainpage(request):
    return HttpResponse('<h1>Sup bro</h1>')