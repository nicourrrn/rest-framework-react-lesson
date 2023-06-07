
run-server:
    python manage.py runserver

migrate:
    python manage.py makemigrations
    python manage.py migrate

build-front:
    cd ui && yarn build 
    cp -r ui/build ./static
