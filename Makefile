up:
	docker-compose -f ./redis-client/docker-compose.yml up -d
	docker-compose -f ./bot/docker-compose.yml up -d