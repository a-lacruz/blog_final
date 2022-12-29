## Sistema de Blog Administrable

Este proyecto esta diseñado para ser un sistema de blog simple donde superusuarios (staff type) 
podran administrar articulos y mensajes de usuarios (registrados y anonimos). 
Algunas de las cosas que se pueden hacer: 

-Crear; ver; actualizar y borrar posts en el blog.
-Crear; ver; borrar mensajes de contacto.
-Registro de usuarios, actualizar perfil, asignar y actualizar avatares.
-Login/Logout para cada usuario.
-Los 5 post mas actuales cronologicamente seran mostrados en una vista inicio.
-Agregar una imagen en cada articulo

### Funcionalidades por Vista

#### DETALLE DE POST:
Despliega un post de la base de datos mostrando los elementos definidos en la vista "Crear Post"

#### LISTA DE POST:
Permite la carga de una lista de los post disponibles en la BD mostrando
lo siguiente dependiendo del tipo de usuario:
##### Staff o SuperUser
    - Crear Post
    - Menu de entrada a vista administracion mensajes de contacto.
    - Actualizar Perfil del usuario logueado.
    - Actualizar Avatar de usuario logueado
    - Ver, Actualizar y Borrar entradas del Blog (Post)
##### Usuario Registrado
    - Actualizar Perfil del usuario logueado. (Filtro que evita cambios a otos usuarios)
    - Cambiar Avatar de usuario logueado. (Filtro que evita cambios a otos usuarios)
    - Ver entradas del Blog disponibles (Post)
##### Usuario Anonimo
    - Ver entradas del Blog disponibles (Post)
#### CREAR POST:
(Registo requerido; Solo disponible para usuarios staff)
Permite CREAR un nuevo post que contenga los siguientes elementos:

    - Titulo
    - Subtitulo
    - Imagen (Max 700px)
    - Texto (texto hasta 4000 caracteres)
#### BORRAR POST:
(Registo requerido; Solo disponible para usuarios staff)
Permite BORRAR cualquiera entrada seleccionada de la base de datos (Post)
#### ACTUALIZAR POST:
(Registo requerido; Solo disponible para usuarios staff)
Permite ACTUALIZAR el contenido de cualquier entrada seleccionada de la base de datos (Post)
#### REGISTRO DE USUARIO:
Permite registrar a un nuevo usuario; dispone de los siguientes campos:

    - Nombre de Usuario
    - Contraseña
    - Confirmacion de Contraseña
#### LOGIN DE USUARIO:
Permite a un usuario previamente registrado ingresar a la aplicacion.
#### LOGOUT DE USUARIO:
Permite a un usuario registrado salir la aplicacion.
#### CAMBIO DE AVATAR:
Permite a un usuario registrado cambiar SOLO su avatar; la asignacion inicial de avatares debe hacerse por el menu administracion
#### ACTUALIZACION DE PERFIL USUARIO:
Permite a un usuario registrado actualizar SOLO los datos de su perfil; dispone de los siguientes campos:

    - Nombre 
    - Apellido
    - E-mail
#### DETALLES DE MENSAJES:
(Registo requerido; Solo disponible para usuarios staff)
Permite VER el detalle de los mensajes enviados por cualquier tipo de usuarios desde el formulario de "contacto".
#### LISTA DE MENSAJES:
(Registo requerido; Solo disponible para usuarios staff)
Permite ver la lista completa de mensajes disponibles en la base de datos, adicionalmente "BORRAR" cualquiera de estos.
#### CREAR MENSAJES:
Permite CREAR un nuevo mensaje a traves del formulario de contacto, que sera visible luego solo para usuarios staff; 
tiene los siguientes elementos:

    - Nombre
    - E-Mail
    - Texto 
    - Texto (texto hasta 4000 caracteres)
Al enviarse de manera correcta; muestra un mensaje en la pantalla.
#### BORRAR MENSAJES:
(Registo requerido; Solo disponible para usuarios staff)
Permite BORRAR cualquier mensaje de contacto seleccionado de la base de datos.
#### Pasos para clonar el proyecto desde Github
Revisa la version de python; este proyecto fue escrito con python 3.11.0, es recomendable que uses la misma version o una superior para evitar problemas de compatibilidades.

Para revisar tu version de python debes desde una terminal, colocar el siguiente comando:

`python --version`
`Python 3.11.0`

Clona el repositorio en tu máquina local utilizando Git. Abre una terminal y escribe:

`git clone https://github.com/usuario/repositorio.git`

Accede al directorio del repositorio clonado:

`cd repositorio`

Asegúrate de tener instalado Django en tu máquina. Si aún no lo tienes instalado, puedes hacerlo ejecutando:

`pip install django`

Instala las dependencias; para esto es necesario que corras en la terminal de tu gestor el comando `pip install`, revisa que estes dentro de la carpeta del proyecto y puedas ver el archivo `requirements.txt`, posteriormente ejecuta al comando:

`pip install -r requirements.txt`

Crea un entorno virtual para el proyecto. Esto te permitirá tener un espacio aislado para instalar las dependencias necesarias para el proyecto y evitar conflictos con otras aplicaciones. Para crear un entorno virtual con Python, puedes utilizar el siguiente comando:

`python -m venv nombre_entorno`

Activa el entorno virtual:
##### En Windows
`nombre_entorno\Scripts\activate.bat`
##### En Linux o macOS
`source nombre_entorno/bin/activate`

Crea la base de datos y ejecuta las migraciones necesarias para crear las tablas y relaciones necesarias para el proyecto:

`python manage.py makemigrations`
`python manage.py migrate`

Arranca el servidor de desarrollo con el siguiente comando:

`python manage.py runserver`

Ahora podrás acceder al proyecto Django desde tu navegador web en la dirección 

`<link>`http://127.0.0.1:8000/.


###### superusers
- admin/admin
- root/root

###### Usuarios regulares
- @PedroPerez/pedro1234
- @MariaLopez/maria1234
- @PastorLopez/pastor1234
