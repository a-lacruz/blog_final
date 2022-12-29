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
Permite a un usuario registrado cambiar su avatar; la asignacion inicial de avatares debe hacerse por el menu administracion
    



###### superusers
- admin/admin
- root/root

###### Usuarios regulares
- @PedroPerez/pedro1234
- @MariaLopez/maria1234
- @PastorLopez/pastor1234
