# Ahoy Indie Media - Django App MVP

User Stories:

- [x] I can add/schedule a video stream (admin)
- [x] I can add/schedule a radio stream (admin)
- [ ] I can view the current radio stream
- [ ] I can view the current video stream
- [ ] I can view all uploaded audio media in a list view
- [ ] I can view all uploaded video media in a list view
- [x] I can view a combined schedule
- [x] I can create an account
- [ ] I can purchase tokens to view content using Stripe
- [ ] I can view my account details and tokens on an account page

## Create virtual environment

```
python3 -m venv env
```

## Activate the virtual environment

```
. env/bin/activate
```

## Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

## Run the server

```
python3 manage.py runserver
```
