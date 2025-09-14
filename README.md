# Sistema de Asistencia Automatizada con Reconocimiento Facial

Este proyecto implementa un sistema básico de **asistencia automatizada** usando la librería [DeepFace](https://github.com/serengil/deepface).  
El sistema reconoce rostros en tiempo real mediante la cámara y registra automáticamente la asistencia en un archivo CSV.

---

## Estructura del proyecto
├── dataset/ # Carpeta que contiene las imágenes de referencia de cada persona
│ ├── persona1.jpg
│ ├── persona2.jpg
│ └── ...
├── asistencia.csv # Archivo generado automáticamente con el registro de asistencia
├── main.py # Script principal del sistema
├── requirements.txt # Dependencias necesarias
└── README.md # Instrucciones y documentación


---

##  Preparación del dataset

1. Crea una carpeta llamada `dataset/` en la raíz del proyecto.  
2. Dentro de `dataset/`, coloca una imagen por cada persona registrada.  
   - El nombre del archivo debe ser el **nombre de la persona**.  
   - Ejemplo:  
     ```
     dataset/Kyle.jpg
     dataset/Ana.jpg
     dataset/Luis.jpg
     ```

---

## Ejecución del proyecto

1. Clona el repositorio y accede a la carpeta del proyecto.  

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>

2. Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate         # En Windows

Instala las dependencias:

pip install -r requirements.txt


Ejecuta el sistema:

python main.py


Ejemplo de salida (asistencia.csv)

El archivo asistencia.csv se genera automáticamente al ejecutar el sistema y tendrá un formato como el siguiente:

Nombre,Hora
Kyle,2025-09-14 10:35:21
Ana,2025-09-14 10:36:05
Luis,2025-09-14 10:38:12


Cada vez que una persona registrada sea reconocida por la cámara, se guardará su nombre y la hora exacta.


Autor

Nombre: Kyle Velázquez

Materia: Inteligencia Artificial

Universidad: Hybridge

