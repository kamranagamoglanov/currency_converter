#!/bin/sh
python3 manage.py makemigrations && sleep 1 && python3 manage.py migrate