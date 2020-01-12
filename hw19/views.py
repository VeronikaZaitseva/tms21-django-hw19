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
    max_comment = list_comment[1]
    for i in range(3):
        if len(list_comment[i])<len(list_comment[i+1]):
            max_comment = list_comment[i+1]
        return HttpResponse(max_comment)


# Дана форма с одним полем - дата. Если дата первое января - вывести
# сообщение: “С новым {номер года} годом”. В ином случае, вывести дату
# в формате: год-месяц-день. Выполнить задание в репозитории из
# первого задания.

def index2(request):
    comment = request.POST.get('comment')
    lenght = len(comment)
    num_vowels = 0
    num_consonants = 0
    for i in range(lenght):
        if comment[i] in list('уеэёоаыяию'):
            num_vowels += 1
        elif comment[i] in list('йцкнгшщзхждлрпвфчсмтбъь'):
            num_consonants += 1
    return HttpResponse(f'Колличество гласных - {num_vowels}. Колличество согласных - {num_consonants}')