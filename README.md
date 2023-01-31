# Ahoy Indie Media - Django App MVP

User Stories:

- [x] I can add a film (admin)
- [x] I can view all uploaded films in a list view
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

# Working with Stripe

Install the [stripe cli](https://stripe.com/docs/stripe-cli)

```
brew install stripe/stripe-cli/stripe
```

