import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace
import cv2

# --- Configuración ---
dataset_path = "dataset"
registros_path = "registros"
asistencia_file = os.path.join(registros_path, "asistencia.csv")

# Crear carpeta registros/ si no existe
os.makedirs(registros_path, exist_ok=True)

# Cargar o crear archivo de asistencia
try:
    asistencia = pd.read_csv(asistencia_file)
except FileNotFoundError:
    asistencia = pd.DataFrame(columns=["Nombre", "Fecha", "Hora"])


print("Sistema de asistencia iniciado. Presiona 'q' para salir.")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    try:
        # Analizar el frame actual con DeepFace
        result = DeepFace.find(img_path=frame, db_path=db_path, enforce_detection=False)

        if len(result) > 0 and not result[0].empty:
            # Tomamos el nombre del archivo más cercano
            identity = result[0]['identity'][0].split("/")[-1].split(".")[0]

            # Fecha y hora actuales
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")

            # Verificar si ya se registró hoy
            if not ((asistencia["Nombre"] == identity) & (asistencia["Fecha"] == fecha)).any():
                asistencia = pd.concat([asistencia, pd.DataFrame([[identity, fecha, hora]],
                                                                 columns=["Nombre", "Fecha", "Hora"])],
                                        ignore_index=True)
                asistencia.to_csv(asistencia_file, index=False)
                print(f"✅ {identity} registrado el {fecha} a las {hora}")

            # Mostrar el nombre en la cámara
            cv2.putText(frame, f"{identity}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    except Exception as e:
        print("Error:", e)

    # Mostrar ventana
    cv2.imshow("Asistencia Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
