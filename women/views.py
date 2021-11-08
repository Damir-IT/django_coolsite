
from django.shortcuts import render, redirect

from django.http import (
    
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    
)
from .models import Women


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request): #HttpsRequest
    return render(
        request, 
        'women/index.html', 
        {
            "posts": Women.objects.all(),
            'menu': menu, 
            'title': 'Главная страница'
        }
    )

def about(request):
  ''' shows about page'''
  return render(request, 'women/about.html', {'menu': menu,'title': 'О сайте'})
    
def archive(request, year):
    if int(year) > 2020:
        raise Http404()
    return HttpResponse(
        
        f'<h1> Архив по годам</h1> \
            <p>{year}</p>'
            
    )

def pageNotFound(request, exception):
    return HttpResponseNotFound(
        '<h1>Вы кто такие? Я вас не звал...</h1>'
    )
       