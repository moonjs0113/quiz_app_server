# Quiz App Server

## Django API Framework
```
// Python 가상 환경 생성
$ python3 -m venv {VENV_NAME}

// 가상 환경 실행
$ source {VENV_NAME}/bin/activate

// Django Rest Framework 설치 
$ pip install django djangorestframework

// Django 프로젝트 생성
$ django-admin startproject {PROJECT_NAME} {DIRECTORY}

// Django 앱 생성
$ python manage.py startapp {APP_NAME}

// 마이그레이션 파일 생성
$ python manage.py makemigrations

// 마이그레이션 반영
$ python manage.py migrate

// Django 서버 실행
$ python manage.py runserver

// Django 관리자 생성
// {domain}/admin
$ python manage.py createsuperuser
```

## Deployment Server to Heroku
```
// 도구 설치
// django-cors-headers : cors 에러 방지 도구
// gunicorn : 배포를 위한 도구
// psycopg2-binary, dj-database-url : postgresql 사용을 위한 도구
// whitenoise : 정적 파일의 사용을 돕는 미들웨어
$ pip install django-cors-headers gunicorn psycopg2-binary whitenoise dj-database-url

// Requirements 문서(패키지 의존성) 생성
$ pip freeze > requirements.txt

// Git Ingnore 생성
$ vi .gitignore 

// Heroku 설치
$ brew install heroku/brew/heroku

// Git Repository 생성
$ git init
...
$ git ush origin master

// Heroku 로그인
$ heroku login

// Heroku 도메인 생성
// https://{DOMAIN}.herokuapp.com/
$ heroku create {DOMAIN}

// Heroku 배포
$ git push heroku master

// Heroku 서버 마이그레이션 파일 생성
$ heroku run python manage.py makemigrations

// Heroku 서버 마이그레이션 반영
$ heroku run python manage.py migrate

// Heroku 서버 관리자 생성
$ heroku run python manage.py createsuperuser

// heroku 서버 실행
$ heroku open
```
