# Social Login Auth
Para *loguearnos* con diferentes redes sociales siempre nos surge una pregunta. ¿Existe alguna librería confiable y lo suficientemente robusta para este trabajo? ¿Debería hacer mi propio *login*?.

En vez de gastar mucho tiempo y esfuerzo en resolver tokens, que si twitter es con *oauth* pero facebook es con otro tipo de authenticación, podemos usar una solución sencilla, práctica y elegante, y esta es la que vamos a usar en este tutorial.


## Python-social-auth
Antes conocida como django-social-auth es una librería increible que te facilita mucho la vida a la hora de querer *loguear* y/o asociar cuentas de redes sociales a los usuarios de nuestros proyectos en django.


### Instalación
---
Para instalar en nuestro proyecto sólo corremos
	
	$ pip install python-social-auth

	
### Registro
---
Para que nuestro proyecto de django se valga de la librería que queremos usar, debemos registrarla en la lista de aplicaciones.

```
INSTALLED_APPS = (
    ...
    'social.apps.django_app.default',
    ...
)
```

Después de esto debemos sincronizar la base de datos para que la librería cree las tablas necesarias para su funcionamiento. Solamente debemos correr en la consola

	$ ./manage.py syncdb


### Configuración
---
La mayoría de redes sociales nos van a pedir dos códigos, un API_KEY y un API_SECRET. Esto es lo primero que debemos *setear* en nuestro *settings.py*.

#### Twitter
Para poder permitir que nuestros usuarios se puedan *loguear* con twitter debemos crear una aplicación. <https://dev.twitter.com/apps/new>. Y establecer las llaves de nuestra aplicación en *settings.py*.

```
SOCIAL_AUTH_TWITTER_KEY = 'mi-consumer-key-de-twitter'
SOCIAL_AUTH_TWITTER_SECRET = 'mi-consumer-secret-de-twitter'
```

#### Facebook
Para facebook es básicamente igual, crear nuestra app en facebook. <https://developers.facebook.com/apps/?action=create>. Y nuevamente decirle a django cuales son nuestras llaves.

```
SOCIAL_AUTH_FACEBOOK_KEY = 'mi-app-id-de-facebook'
SOCIAL_AUTH_FACEBOOK_SECRET = 'mi-app-secret-de-facebook'
```
**Nota**

Si en facebook queremos traer información adicional de los usuarios debemos configurar en *settings.py*. Por ejemplo, si deseamos que facebook nos devuelva el email de los usuarios debemos escribir

	SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

Debido a que el email no es un campo que se obtenga por defecto, debemos pedir el permiso para usarlo.
> Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by deafault, to get it, you must request the email permission.


### Backends
---
Esta librería soporta una buena cantidad de *backends* entre los que se destacan:

* Amazon
* Dailymotion
* Dropbox
* Evernote
* Facebook
* Flickr
* Foursquare
* Github
* Google
* Instagram
* Rdio
* Reddit
* Soundcloud
* Stackoverflow
* Steam
* Stripe
* Twitter
* Yahoo

Ahora debemos decirle a la librería cuáles *backends* o redes sociales queremos usar en *settings.py*.

```
AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    ...
    'django.contrib.auth.backends.ModelBackend',
)
```
**Nota**

Si no incluímos ``'django.contrib.auth.backends.ModelBackend'`` al final de nuestros *backends*, los usuarios no podrán *loguearse* con usuario y contraseña.


### URLs
---
En cuanto a la configuración de las URLs tenemos cubierto casi todas las opciones posibles en cuanto a *login* se trata. 

```
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined.
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'
```

Podemos agregar todas o sólo una para cada caso que nosotros queramos utilizar. Para nuestro ejemplo usaremos **dos** en *settings.py*.

```
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'
```

Adicional a esto tenemos que habilitar las URLs con las que vamos a *loguear* a los usuarios. Esto lo hacemos en *urls.py*.

	url('', include('social.apps.django_app.urls', namespace='social'))


### Template
---
Por último sólo nos resta colocar los enlaces para que nuestros usuarios se puedan *loguear*.

```
<a href="{% url 'social:begin' 'twitter' %}">Twitter</a>
<a href="{% url 'social:begin' 'facebook' %}">Facebook</a>
```
