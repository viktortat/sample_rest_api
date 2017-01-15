#Тестовое задание для backend разработчика

Для обеспечения возможности общения с сервером через RES API в макете используются  Django и Django Rest Framework. База данных, состоящая из индентификатора («uid») и логина («login») создана средствами Django ORM.

Django Rest Framework обеспечивает возможность выполнять запросы через браузер или через любой commandline клиент — curl, wget, httpie и пр.

Примеры запросов для httpie:
    - Создание пользователя: http POST http://127.0.0.1:8000/users/ uid=3 login="Test"
    - Cписок всех пользователей: http GET http://127.0.0.1:8000/users/
    - Поиск по имени: http GET http://127.0.0.1:8000/users/?search=vl
    - Поиск по идентификатору: http GET http://127.0.0.1:8000/users/1/
    - Удаление по идентификатору:  http DELETE http://127.0.0.1:8000/users/3/
    - Обновление имени по идентификатору: http PUT http://127.0.0.1:8000/users/1/ uid=1 login="Vlad"
