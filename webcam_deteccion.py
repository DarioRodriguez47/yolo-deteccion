"""Deteccion de objetos en tiempo real con YOLOv8n usando la camara del PC."""
import cv2
from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("No se pudo abrir la camara (indice 0)")
        return

    print("Presiona 'q' para salir")
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model(frame, verbose=False)
        annotated = results[0].plot()

        cv2.imshow("YOLOv8 - Deteccion en vivo", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
