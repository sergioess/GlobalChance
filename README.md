<h2>GlobalChance </h2>

<p> GlobalChance se enfoca en generar conciencia ambiental, permitirá visualizar datos verídicos de los cambios de temperatura a nivel nacional. Dirigido a la población absoluta, niños, jóvenes y mayores.
</p>
<p>
  Es bien sabido que estos datos se pueden visualizar en tiempo real en las páginas de información pública.
GlobalChange le ayuda a visualizar los datos de forma dinámica y sencilla además, incentiva a la comunidad a hacer un cambio en su propia familia dándole ideas útiles para hacerlo, para disminuir la emisión de GEI.

</p>

<h3>Descripción del Proyecto</h3>

<p>El proyecto se desarrolló en Lenguaje Python haciendo uso del Framework Flask. La base de datos seleccionada para el proyecto fue PostgresSQL, la cual fue desplegada en la plataforma Heroku de forma gratuita. </p>
<br>
<p>Las librerías usadas en el Backend fueron:</p>
<li>bcrypt==3.2.0 : Para encriptar las contraseñas de los Usuarios registrados</li>

<li>Flask-Login==0.5.0: Para el manejo del Inicio de Sesión y usuario registrado</li>

<li>Flask-Session==0.4.0: Para mantener la sesión de un usuario logueado abierta .</li>

<li>Flask-SQLAlchemy==2.5.1: Para realizar las consultas a la base de datos</li>

<li>psycopg2==2.9.2: Driver para usar PostgreSQL en la aplicación</li>
<br>
<p>Para el Frontend usamos:</p>
<li>Bootstrap: Para aplicar estilos a la página</li>

<li>Chart.js: Para generar las gráficas dinámicas </li>

<li>Datatables: Para mostrar los datos, permitiendo filtros, paginación e reportes</li>

<li>Jquery: Necesario para algunos librerías como bootstrap</li>

<li>Ajax: Para traer los datos que se usan para graficar</li>

<li>Google Fonts: Para aplicar una fuente al proyecto</li>
<br>

<p>Propusimos el uso de tres perfiles, un Usuario general, Usuario Editor y Administrador. Toda persona que se registra en la Aplicación, por defecto es asignado al perfil usuario, el cual le permite visualizar y consultar las gráficas generadas así como los banners que presentan información de interés general.</p>
<br>
<p>El Usuario Editor, es un tipo de usuario asignado a instituciones o entes del gobierno cuyo fin es el de registrar la temperatura actual de la ciudad que reside.  El Usuario Editor también tiene los privilegios de usuario. El Usuario Editor sólo puede ver los registros ingresados por él, las gráficas de consulta utilizan todos los registros de la Base de Datos no sólo los del Usuario para generar las gráficas.</p>
<br>
<p>El Usuario Administrador tiene acceso al listado de todos los usuarios registrados. Desde esta vista, puede cambiar de perfil de un Usuario a perfil Editor, también puede ocultar usuarios.  Otra funcionalidad del Perfil Administrador es subir a la página los banners informativos que van a poder visualizar los usuarios de Perfil “Usuario General” y “Usuario Editor”. Desde ahí puede subir una imágen, un título y un texto tipo descripción.</p>
<br>
<br>
<p>Se inició con dos ciudades: Bucaramanga y Medellín ya que lo importante en este momento es proveer la funcionalidad de la aplicación, ya en producción, se pueden incluir las otras ciudades principales de Colombia. Se obtuvieron datos iniciales de la página de datos abierta (https://www.datos.gov.co) que pone el Estado para consulta. Hicimos un filtro en esa página, posteriormente los datos filtrados los descargamos en un archivo csv, lo importamos a excel y eliminamos las columnas que no necesitábamos y por último generamos una consulta Insert con la función de excel Concatenar (“insert into registro_temperatura (fecha_registro, temperatura_aire, id_usuario, id_ciudad, year,mes) values ('20170927 22:38:34.389',22.3,13,1,2017,09)”) y pegamos todos los insert a DBeaver para ejecutar las consultas a la Base de Datos. De “Datos Abiertos” subimos un poco más de 5300 registros en la base de datos.</p>

