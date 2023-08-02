from django.shortcuts import render
from django.http import HttpResponse # подключаю класс для ответа
# создаю классы или функции которые по запросу будут возвращать ответ
def index(request):
    return HttpResponse("Домашка по 4 занятию")
