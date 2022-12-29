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

##### Detalle de Post:
Despliega un post de la base de datos mostrando lo siguiente:
    - Titulo
    - Subtitulo
    - Imagen (Max 700px)
    - Texto (texto hasta 4000 caracteres)
##### Lista de Post:
Permite la carga de una lista de los post disponibles en la BD mostrando
lo siguiente dependiendo del tipo de usuario:
##### Staff o SuperUser
    - Crear Post
    - Menu de entrada a vista administracion mensajes de contacto.
    - Actualizar Perfil del usuario logueado.
    - Actualizar Avatar de usuario logueado
    - Ver, Actualizar y Borrar entradas del Blog (Post)
#### Usuario Registrado
    - Actualizar Perfil del usuario logueado. (Filtro que evita cambios a otos usuarios)
    - Cambiar Avatar de usuario logueado. (Filtro que evita cambios a otos usuarios)
    - Ver entradas del Blog disponibles (Post)
#### Usuario Anonimo
    - Ver entradas del Blog disponibles (Post)





###### superusers
- admin/admin
- root/root

###### Usuarios regulares
- @PedroPerez/pedro1234
- @MariaLopez/maria1234
- @PastorLopez/pastor1234
