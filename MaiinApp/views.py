from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

author = {'name': 'Ivan_Petrovich',
          'surname': 'Ivanov',
          'phone': '8-923-600-01-02',
          'email': 'vasya@mail.ru'}

items = [
    {'id': 1, "name": "Кроссовки abibas" ,"quantity": 5},
    {'id': 2, "name": "Куртка кожаная" ,"quantity": 2},
    {'id': 5, "name": "Кока-кола 1 литр" ,"quantity": 12},
    {'id': 6, "name": "Картошка фри" ,"quantity": 0},
    {'id': 8, "name": "Кепка" ,"quantity": 124},
]


# Create your views here.
def home(request):
    context = {
        "name": 'Петров Николай Иванович',
        "email": "kolya@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    result = f"""
        Имя: <b>{author['name']}</b></br> 
        Фамилия: <b>{author['surname']}</b></br> 
        телефон: <b>{author['phone']}</b></br> 
        email: <b>{author['email']}</b></br>
        """
    return HttpResponse(result)

def get_item(request, id):
    # print(f'{id = }, {type(id) = }')
    #
    for item in items:
        if item['id'] == id:
            """По указанному ай-ди функция возвращает имя и кол-во"""
            result = f"""
            <h2>Имя: {item["name"]} </h2>
            <p>Количество: {item['quantity']} </p>
            <a href='/items'> Назад </a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id={id} not found')

def items_list(request):
    # result = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        "items": items
    }
    # Аргументы рендера: запрос, имя файла шаблона, контекст (чем заполняем)
    return render(request, "items-list.html", context)




