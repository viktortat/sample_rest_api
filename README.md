# Тестовое задание для backend разработчика

Для обеспечения возможности общения с сервером через RES API в макете используются  Django и Django Rest Framework. База данных, состоящая из индентификатора («uid») и логина («login») создана средствами Django ORM.

Django Rest Framework обеспечивает возможность выполнять запросы через браузер или через любой commandline клиент — curl, wget, httpie и пр.

Примеры запросов для httpie:
- Создание пользователя: <b>http POST http://127.0.0.1:8000/users/ uid=3 login="Test"</b>
- Cписок всех пользователей: <b>http GET http://127.0.0.1:8000/users/</b>
- Поиск по имени: <b>http GET http://127.0.0.1:8000/users/?search=vl</b>
- Поиск по идентификатору: <b>http GET http://127.0.0.1:8000/users/1/</b>
- Удаление по идентификатору: <b>http DELETE http://127.0.0.1:8000/users/3/</b>
- Обновление имени по идентификатору: <b>http PUT http://127.0.0.1:8000/users/1/ uid=1 login="Vlad"</b>
