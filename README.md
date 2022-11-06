# django_bootstrap
https://www.udemy.com/course/django-em-120-minutos


## Creating a new SECRET_KEY for Django settings
1. Setup a new secret environment variable where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:

```
python
import secrets
secrets.token_urlsafe(32)
```

In this project we use Python-Decouple librarie to setting it, for this you need create a file ".env" and inform generate your SECRET KEY. Example:
```
# DJANGO
SECRET_KEY=your_secret_key_with_32_bits
```