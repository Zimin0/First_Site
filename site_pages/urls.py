from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home, name = 'home'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('<str:pagename>', views.index, name='index'),
]



# Поскольку функция path () не может захватывать пустую строку, мы должны создать специальный вариант для домашней страницы, что мы и делаем в строке 7. Когда пользователь переходит к корню сайта, строка 7 устанавливает pagename в пустую строку (' ').