run: 	
	python3 manage.py runserver

mg: 
	python3 manage.py makemigrations && sleep 1 && python3 manage.py migrate

redis:
	redis-server

worker:
	celery -A currency_converter  worker -l INFO

beat:
	celery -A currency_converter  beat -l INFO
