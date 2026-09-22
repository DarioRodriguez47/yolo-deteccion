import cv2
from ultralytics import YOLO

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("ERROR: no se pudo abrir la camara (indice 0)")
        return False

    ok, frame = cap.read()
    cap.release()
    if not ok:
        print("ERROR: la camara se abrio pero no devolvio un frame")
        return False

    print(f"Camara OK, frame shape: {frame.shape}")

    model = YOLO("yolov8n.pt")
    results = model(frame)
    annotated = results[0].plot()
    cv2.imwrite("test_deteccion.jpg", annotated)
    print("Deteccion OK, guardada en test_deteccion.jpg")
    print(f"Objetos detectados: {len(results[0].boxes)}")
    return True

if __name__ == "__main__":
    main()
