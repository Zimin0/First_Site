from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Lang_Page

def home(request): # delete !!!!
    return render (request, 'base.html')

def index(request, pagename): 
    pagename = '/' + pagename
    pg = get_object_or_404(Lang_Page, permalink=pagename) 
    context = {
        'main_title': pg.main_title,

        'title_1': pg.title_1,
        'content_1': pg.content_1,

        'title_2': pg.title_2,
        'content_2': pg.content_2,

        'title_3': pg.title_3,
        'content_3': pg.content_3,

        'title_4': pg.title_4,
        'content_4': pg.content_4,

        'page_list': Lang_Page.objects.all(), # добавил переменную page_list в контекст и добавил в нее страницы из нашей базе данных.
    }
    return render (request, 'pages/lists.html', context) 
