![example workflow](https://github.com/Ulyana819/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

адрес сайта http://178.154.203.121/admin/
# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
## Автор   
:paperclip: Ульяна Шмакова    
## Технологии
:paperclip: guniorn
:paperclip: Nginx
:paperclip: Docker
:paperclip: Docker-compose
:paperclip: PostgreSQL

## Запуск контейнера и приложения в нем

### Перейти в репозиторий для запуска докера
cd infra/

### Запуск docker-compose
docker-compose up -d --build

### После создайте суперпользователя
docker-compose exec web python manage.py createsuperuser

### Войдите в админку и создайте одну-две записи объектов

### При необходимости можно создать дамп (резервную копию) базы:
docker-compose exec web python manage.py dumpdata > fixtures.json
