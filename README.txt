_____________________________________________________
SECCION 1
## Entorno Virtul
    https://www.youtube.com/watch?v=e6PkGDH4wWA

1 verificar version de python instalado  python --version
2 crear entorno virtual 
    py -m venv venv
    crea una carpeta venv

    ACTIVARLO
    f1 + python select interpete y luego al abrir una consola ya ver con (VENV)
    con la palabra desactivate
    otra forma es 
    .\venv\Scripts\activate


3 Instalar DJANGO con:  pip install django
4 verificar la version django-admin --version

5 Crear proyecto
    django-admin startproject djangoCrud .

6 ejecutar el proyecto :   python manage.py runserver
_____________________________________________________
SECCION 2
aplicacion: Carpeta general se llama djangocrud , luego tenemos que tener apliucacuiiones 
dstintas por ejemplo paginas priuncipales , otra parte seria el main y ora parte el blog todas son aplicaciones que son 
parte del mismo proyecto

Creamos una nueva aplicacion dento del proyecto
Ejecutar la aplicacion:    python manage.py startapp task
Luego se registra en la carpeta printicpal en nuestro caso seria djangocrud en setting.py INSTALLED_APP

Luego en View de task creo un heloword

Luego ingreso a la aplucacion pdjgocrud en url y la llamo


Arranco la apliucacion : python manage.py runserver
_____________________________________________________
SECCION 3
Crear formulario (min10)
En task crear carpeta template para generar las paginas html
creo el archivo singup para login
jinga motor de plantillas de djnago

Para la migracion 
python manage .migrate  genera las tablas en sqlite
_____________________________________________________
SECCION 4

Creo un usuario super administrador 
python manage.py createsuperuser
diegof
diegof

Luego que crear una tabla correr 
python manage.py makemigrations  
python manage.py migrate 


_____________________________________________________
SECCION 5
Subir a Git
https://dashboard.render.com/

1. render.com --> Servicio web
2. setings ->SECRET_KEY  importarla 
3.DEBUG = False , DEBUG = 'RENDER' not in os.environ detecta si esta en produccion o desa
4.RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')  (lee la variable y retorina un valor si existe el alow host lo llena con la IP)
5.if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
6.Instalar una variable para la base de datos del servidor de la nube : pip install dj-database-url
7.Instalar este modulo para posgrate se pueda conectar pip install psycopg2-binary 
8. servidor se instala pip install whitenoise
    añadir al midlerware
9. agregar sentencias luego de STATIC_URL para debug
10. buid sh para linux
11. pip install gunicorn
12. pip freeze > requirements.txt

GIT 
0.1 si quiero borraro es del.git y luego Y 
1. Archivo .gitignore
2. git init
3. git add .
4. git commit -m "first commit"
5. https://github.com/diegofer10
6. Crear repo 
7. copiar git remote add origin https://github.com/diegofer10/django-auth-crud.git
8. git push -u origin master


Si realizo un Cambio 
1. git status
2. git add . 
