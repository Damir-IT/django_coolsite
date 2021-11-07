
from django.shortcuts import render, redirect

from django.http import (
    
    HttpResponse,
    HttpResponseNotFound,
    Http404,

)

def index(request): #HttpsRequest
    return HttpResponse('Страница приложения women')

def categories(request, catid):
    if int(catid) > 3:
        return redirect('home', permanent=True)
    
    return HttpResponse(
        
        f'<h1>Статьи по категориям</h1> \
        <p>{catid}</p>'
        
    )
    
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
       