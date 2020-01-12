from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# Дана форма с тремя текстовыми полями. Вернуть пользователю максимальное
# по длине значение поля. Пример: введены abc, abcdef, ab - пользователю
# вернется abcdef. Для задания требуется создать новый репозиторий.

def index1(request):
    comment1 = request.POST.get('comment1')
    comment2 = request.POST.get('comment2')
    comment3 = request.POST.get('comment3')
    list_comment = (comment1, comment2, comment3)
    max_comment = list_comment[0]
    for i in range(3):
        if len(max_comment) < len(list_comment[i]):
            max_comment = list_comment[i]
    return HttpResponse(max_comment)


# Дана форма с одним полем - дата. Если дата первое января - вывести
# сообщение: “С новым {номер года} годом”. В ином случае, вывести дату
# в формате: год-месяц-день. Выполнить задание в репозитории из
# первого задания.

def index2(request):
    index_date = request.POST.get('date')
    date1 = datetime.strptime(index_date, '%Y-%m-%d')
    nyd = date1.strftime('%Y-01-01')
    if date1 == datetime.strptime(nyd, '%Y-%m-%d'):
        return HttpResponse(f'С новым {date1.year} годом!')
    else:
        return HttpResponse(f'{date1.year}-{date1.month}-{date1.day}')

