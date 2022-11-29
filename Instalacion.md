Para el funcionamiento del proyecto necesitas:

1-> Python v: 3.10.7
2-> pip 

3 Django v:4.1.2
4 Pillow v: 9.2.0

Instrucciones de Instalacion:

1-Instalar python con la version adecuada

2- Crear un entorno virtual:
    
    ---- python -m venv venv 
3- Instalar los paquetes de django

    --- pip install -r requeriments.txt 
Esto instalara django y pillow en su version correspondiente automaticamente

4-(opcional) Instalar un gestor de bases de datos relacional

Configuracion:

1- En Alexandria/Alexandria/settings.py :

    Asigna una secret key(la que quieras)
    
    Configura tu base de datos(Si no instalaste ninguna debes poner lo siguiente adentro del diccionario llamado DATABASES):
        
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
         } 

    En caso de haber instalado alguna en esta pagina estan las configuraciones:

        https://docs.djangoproject.com/es/4.1/ref/databases/

2- Entra al entorno virtual usando este comando en la carpeta del projecto:

        .venv/Scripts/activate

3- Dentro de: /Alexandria/:

    python manage.py makemigrations
    python manage.py migrate

4- Abre tu bases de datos e inserta los datos en /Develop Database Inputs/

Correr Proyecto:

1-Entra en el entorno virtual

2-En /Alexandria/:

    python manage.py runserver


