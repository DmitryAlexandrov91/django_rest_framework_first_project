<div align="center">
<h1> DRF Api </h1>
<p><em>Первое знакомство с Django Rest Framework</em></p>
</div>

▌ Описание ℹ️

Простое API приложение на Django Rest Framework. 
Представляет собой APi взаимодействие с условным сервисом по публикации постов.

Проект наглядно демонстрирует мощные встроенные возможности DRF, такие как:

- аутентификация пользователей
- сериализация данных
- представления для эндпоинтов (viewsets)
- разграничение прав доступа


---

▌ Установка и запуск 🛠️


Склонируйте репозиторий, разверните виртуальное окружение и установите зависимости из файла requirements.txt


Перейдите в директорию blogicum

`cd /yatube_api`

Примените миграции

`python manage.py migrate`

Создайте суперюзера для доступа к админ зоне приложения

`python manage.py createsuperuser` # Выполните все необходимые шаги в терминале

Запустите приложение

`python manage.py runserver`

Благодаря возможностям подключенной библиотеки drf-spectacular, вы можете протестировать работу API приложения через web интерфейс:

*http://127.0.0.1:8000/api/docs/*


---
▌ Автор 📝

Александров Дмитрий

<u>GitHub</u>
 - https://github.com/DmitryAlexandrov91

 <u>Telegram</u>
 - https://t.me/@AlDmAl

  <u>Habr Career</u>
 - https://career.habr.com/aldmal