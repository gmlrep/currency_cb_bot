# Чат-бот для отображения актуального курса валют с ЦБ РФ


### Запуск через Makefile:
```bash
make up
```

### Запуск через Docker-compose:
```bash
docker network create bot-redis-network
docker-compose -f ./redis-client/docker-compose.yml up -d
docker-compose -f ./bot/docker-compose.yml up -d
```