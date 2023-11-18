from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client  # Импортируйте модель данных Client

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse


# Create your views here.
def your_form_list(request):
    users = User.objects.all()
    # Применяем фильтры
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(first_name__icontains=search_query) | users.filter(username__icontains=search_query)

    # Добавляем пагинацию
    paginator = Paginator(users, 10)  # 10 объектов на странице
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'Users': users,
        'search_query': search_query,
    }

    return render(request, 'main/doks_list.html', context)


# Функция ВХОДА в систему
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # auth
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')
            return redirect('main')
    else:
        pass
    return render(request, 'main/login_page.html')


# Функция РЕГИСТРАЦИИ в системе
def register(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        username = request.POST.get('username')  # Получаем имя из формы
        email = request.POST.get('email')  # Получаем email из формы
        first_name = request.POST.get('first_name')  # Получаем имя из формы
        last_name = request.POST.get('last_name')  # Получаем фамилию из формы

        if password1 == password2:
            # Проверяем, существует ли пользователь с таким логином или email
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'Пользователь с таким логином или email уже существует.')
            else:
                # Создаем нового пользователя и сохраняем в базу данных
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                messages.success(request, 'Вы успешно зарегистрированы и вошли в систему.')
                return redirect('main')
        else:
            messages.error(request, 'Введенные пароли не совпадают.')
    return render(request, 'main/login_page.html')


# Функция ВЫХОДА из системы
def logout_user(request):
    logout(request)
    return redirect('main')


# Функция для запуска страницы work.html
# c передачей данных на эту страницу
def work(request):
    clients = Client.objects.all()
    users = User.objects.all()

    return render(request, 'main/work.html', {'clients': clients, 'users': users})


def client(request):
    clients = Client.objects.all()
    return render(request, 'main/client.html', {'clients': clients})


# страница сотрудников + пагинация
def user(request):
    users = User.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(first_name__icontains=search_query) | users.filter(
            username__icontains=search_query) | users.filter(email__icontains=search_query) | users.filter(
            last_name__icontains=search_query)

    # Упорядочиваем QuerySet
    sort_by = request.GET.get('sort_by', 'id')  # По умолчанию сортируем по id
    direction = request.GET.get('direction', 'asc')  # По умолчанию сортировка по возрастанию

    order_by = sort_by if direction == 'asc' else f"-{sort_by}"

    users = users.order_by(order_by)

    paginator = Paginator(users, 5)  # 10 объектов на странице
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    # paginator = Paginator(users, 15)
    # page = request.GET.get('page')
    # users = paginator.get_page(page)

    page_number = users.number
    page_range = range(max(1, page_number - 2), min(users.paginator.num_pages, page_number + 2) + 1)

    context = {
        'users': users,
        'page_range': page_range,
        'search_query': search_query,
        'sort_by': sort_by,
        'direction': direction,
    }

    return render(request, 'main/more_users.html', context)


def docks_list(request):
    return render(request, 'main/doks_list.html')


def client_exists(request):
    users = User.objects.all()
    return render(request, 'main/client_exists.html', {'users': users})


# Функция открытия страницы о клиенте
def client_details(request, client_id):
    # Получаем объект пользователя по client_id
    client_d = get_object_or_404(Client, pk=client_id)

    # Отправляем объект пользователя в шаблон
    return render(request, 'main/client_details.html', {'client': client_d})


# Функция открытия страницы о сотруднике
def user_details(request, user_id):
    # Получаем объект пользователя по user_id
    user_d = get_object_or_404(User, pk=user_id)

    # Отправляем объект пользователя в шаблон
    return render(request, 'main/user_details.html', {'user': user_d})


# Функция создания клиента
def create_client(request):
    if request.method == 'POST':
        # Обработка данных, отправленных POST-запросом
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        organization_name = request.POST.get('organization_name')
        inn = request.POST.get('inn')
        bank_account = request.POST.get('bank_account')
        organization_address = request.POST.get('organization_address')
        telegram_nickname = request.POST.get('telegram_nickname')
        description = request.POST.get('description')
        integer_field_1 = request.POST.get('integer_field_1')
        integer_field_2 = request.POST.get('integer_field_2')

        existing_client = Client.objects.filter(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            contact_number=contact_number,
            email=email,
            # Добавьте другие поля для проверки
        ).first()  # Если клиент существует, получите его, в противном случае вернется None

        if existing_client:
            # Клиент уже существует, можете выполнить какое-либо действие, например, выдать ошибку
            return render(request, 'main/client_exists.html')
        # Другие поля

        # Создание нового клиента и сохранение его в базе данных
        clientt = Client(first_name=first_name, last_name=last_name, middle_name=middle_name,
                         contact_number=contact_number, email=email, organization_name=organization_name,
                         inn=inn, bank_account=bank_account, organization_address=organization_address,
                         telegram_nickname=telegram_nickname, description=description, integer_field_1=integer_field_1,
                         integer_field_2=integer_field_2)
        clientt.save()

        return redirect('client')  # Здесь укажите URL для перенаправления после успешного создания клиента

    return render(request, 'main/client.html')
