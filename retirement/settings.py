"""
Django settings for retirement project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os


















import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


# Baseline configuration.
AUTH_LDAP_SERVER_URI = 'ldap://35.199.81.116'

AUTH_LDAP_BIND_DN = 'cn=admin,dc=arqsoft,dc=unal,dc=edu,dc=co'
AUTH_LDAP_BIND_PASSWORD = 'admin'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'ou=academy,dc=arqsoft,dc=unal,dc=edu,dc=co',
    ldap.SCOPE_SUBTREE,
    '(uid=%(user)s)',
)
# Or:
# AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=arqsoft,dc=unal,dc=edu,dc=co'

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'ou=academy,dc=arqsoft,dc=unal,dc=edu,dc=co',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfNames)',
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=academy,ou=groups,dc=arqsoft,dc=unal,dc=edu,dc=co'
AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=academy,ou=groups,dc=arqsoft,dc=unal,dc=edu,dc=co'

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': 'cn=active,ou=academy,ou=groups,dc=arqsoft,dc=unal,dc=edu,dc=co',
    'is_staff': 'cn=staff,ou=academy,ou=groups,dc=arqsoft,dc=unal,dc=edu,dc=co',
    'is_superuser': 'cn=superuser,ou=academy,ou=groups,dc=arqsoft,dc=unal,dc=edu,dc=co',
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguised names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
















# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'um%wk#p^m@!&bc1do@2prsl=fsp5mbk@*21e@rgnuw7*9g3q(o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'employees',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'retirement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'retirement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


#LOCAL DATABASE
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#MY MYSQL DATABASE
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'gestioninterna',
#        'USER': 'root',
#        'PASSWORD': '123456',
#    }
#}

#DOCKER DATABASE
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql', #django.db.backends.mysql 
#        'NAME': 'gestioninterna', #local: libraries #server: 
#        'USER': 'root', #root #root
#        'PASSWORD': '123456', #local: root #server: 
#        'HOST': 'db', #local: localhost  #server:
#        'PORT': '3309',
#    }
#}

#REMOTE DATABASE
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql', #django.db.backends.mysql 
#        'NAME': 'shape_retirement', #local: libraries #server: 
#        'USER': 'shape_retirem', #root #root
#        'PASSWORD': 'Ret2018@', #local: root #server: 
#        'HOST': '69.55.59.217', #local: localhost  #server:
#        'PORT': '',
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #django.db.backends.mysql 
        'NAME': 'shape_retirement', #local: libraries #server: 
        'USER': 'generic_test', #root #root
        'PASSWORD': 'Arquitectura2018', #local: root #server: 
        'HOST': '107.180.54.252', #local: localhost  #server:
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
