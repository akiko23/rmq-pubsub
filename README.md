## Инструментальные средства разработки ПО
## Практическое задание номер 2

### Установка

1. Клонируйте репозиторий
```
git clone https://github.com/akiko23/rmq-pubsub
```

2. Зайдите в папку с проектом и пропишите
```
cd rmq-pubsub
docker-compose up -d
```

3. После запуска контейнеров для проверки можно ввести
```
docker exec -it rmq_pubsub-cassandra cqlsh -e "USE data; SELECT * FROM messages1; SELECT * FROM messages2;"
```

Выполнил: Василенко Дмитрий К070922
