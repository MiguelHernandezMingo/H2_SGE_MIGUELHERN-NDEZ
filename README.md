Descripción
Este proyecto es una aplicación diseñada para gestionar encuestas. Los usuarios pueden crear encuestas, responderlas, y almacenar los resultados en una base de datos MySQL. La aplicación incluye formularios de entrada para la recopilación de datos, validación de entradas y la capacidad de agregar, editar y eliminar registros de encuestas. Está desarrollada en Python utilizando la biblioteca mysql-connector para la conexión y manejo de la base de datos.

Objetivo
El objetivo principal de este proyecto es permitir a los administradores gestionar fácilmente encuestas en línea y almacenar las respuestas de los usuarios en una base de datos. Se busca proporcionar una interfaz sencilla y funcional para realizar las siguientes acciones:

Crear una nueva encuesta.
Responder a encuestas existentes.
Validar y manejar correctamente los datos ingresados.
Conectar con una base de datos MySQL para almacenar las respuestas.
Tecnologías utilizadas
Lenguaje de programación: Python
Base de datos: MySQL
Bibliotecas:
mysql-connector: para la interacción con la base de datos MySQL.
Tkinter: para la creación de una interfaz gráfica de usuario (GUI).
Funcionalidades
Ingreso de Encuestas: Permite a los usuarios crear encuestas con campos como nombre, edad y otras opciones personalizables.
Validación de datos: Asegura que la información ingresada sea correcta, especialmente validando que la edad sea un valor numérico entero.
Conexión a base de datos: Los datos se almacenan en una base de datos MySQL, permitiendo la consulta y manipulación de los registros.
Interfaz gráfica: Se utiliza una interfaz gráfica sencilla con botones para agregar, editar o eliminar registros.
Uso
Para usar la aplicación, sigue estos pasos:

Clona este repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/tuusuario/encuestas.git
Instala las dependencias necesarias:

bash
Copiar código
pip install mysql-connector tkinter
Configura la base de datos MySQL:

Crea una base de datos llamada encuestas en MySQL.
Asegúrate de que las credenciales de conexión (usuario, contraseña, etc.) estén correctamente configuradas en el script de conexión.
Ejecuta la aplicación:

bash
Copiar código
python app.py
Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:

Haz un fork de este repositorio.
Crea una rama nueva (git checkout -b nueva-funcionalidad).
Realiza los cambios y haz commit de ellos (git commit -am 'Añadir nueva funcionalidad').
Haz push de tus cambios a tu fork (git push origin nueva-funcionalidad).
Abre un pull request para que los cambios sean revisados y fusionados.
