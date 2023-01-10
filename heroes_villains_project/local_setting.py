# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tn(ewz$9%n9eko-70#!gfhmi)hl1))zig8g#cg8du4kzbl+7&_'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}