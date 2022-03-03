# Проектная работа
Тестовое задание на позицию Junior Python Developer abz.agency

[Текст задания](https://drive.google.com/file/d/1qUzx0m_Koj83k_G8BScCNK7opazbuDzk/view)


[Доступна демо версия сайта](https://.....).


## Установка
Python 3+ должен быть установлен.

Установите программу из репозитория GitHub:
```bash
git clone https://github.com/evgeniya35/Project_Employees.git

```

Установите зависимости
```bash
pip install -r requirements.txt
```
Настройте переменные окружения в файле `.env` (рядом с файлом `manage.py`):
```
SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
STATIC_ROOT=staticfolder

# postgres DB settings
DB_NAME=emp
DB_USER=emp
DB_PASSWORD=***
DB_HOST=127.0.0.1
DB_PORT=5432
```

Создайте начальную базу данных:
```bash
python manage.py migrate
```

## Запуск

Сформируйте тестовый набор данных командой:
```bash
python manage.py load_emp 1000
```
(1000 количество сотрудников).

Запустите локальный сервер:
```bash
python manage.py runserver
```
Перейдите в адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).


Файлы с данными профессий взят [отсюда](https://github.com/johnlsheridan/occupations.git).


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).