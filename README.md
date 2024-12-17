# Gestor de Tareas

## Descripción
**Gestor de Tareas** es una aplicación desarrollada en Python para la creación, gestión y exportación de tareas. Esta herramienta permite:

- Crear y gestionar tareas de manera sencilla.
- Visualizar y administrar tareas mediante una interfaz gráfica.
- Exportar las tareas a un archivo en formato **JSON** para un manejo más flexible y portable.

## Características Principales
- **Interfaz Visual**: Implementada usando **Streamlit**, que facilita la visualización y uso de la aplicación.
- **Base de Datos**: Utiliza **SQLAlchemy** para la creación y manejo de la base de datos.
- **Exportación de Datos**: Se utiliza la librería **JSON** para exportar tareas a archivos JSON.

## Tecnologías Utilizadas
- **Lenguaje de Programación**: Python 3
- **Interfaz Gráfica**: Streamlit
- **Base de Datos**: SQLAlchemy
- **Gestor de Archivos**: JSON

## Configuración del Entorno de Desarrollo
Para garantizar la portabilidad y el correcto funcionamiento de la aplicación, es necesario configurar un entorno virtual y recuperar las dependencias desde el archivo `requirements.txt`.

### Creación del Entorno Virtual
1. Crea el entorno virtual ejecutando el siguiente comando:
   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - **En Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **En Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

### Instalación de Librerías
Una vez activado el entorno virtual, instala las dependencias necesarias utilizando el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Archivo `requirements.txt`
El archivo incluye las siguientes librerías principales:
- **streamlit**: Permite construir una interfaz visual rápidamente.
- **sqlalchemy**: Manejo de bases de datos con Python.
- **json**: Librería nativa de Python para trabajar con archivos JSON.

### Ejecución de la Aplicación
Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:
```bash
streamlit run app.py
```

### Resultado en SonarQube

![Imagen 1](img\sonarqube_1.png)
![Imagen 2](img\sonarqube_2.png)

## Autor
Desarrollado por Fabian Esteban Becerra Gonzalez © 2024.