# Django App

## Install

- docker
- git

```bash
apt update && apt install git curl -y
curl -fsSL https://get.docker.com | bash
```

## configure

```bash
cd /opt
git clone https://gitlab.com/myskillbox_learn/app_django.git
cd app_django/
cp .env.template .env
openssl rand -hex 32
```

## start app

```bash
docker compose build app
docker compose up -d app
docker compose exec app python manage.py migrate
docker compose exec app python manage.py createsuperuser
```
