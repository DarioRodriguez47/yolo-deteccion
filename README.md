# yolo-deteccion

Deteccion de objetos en tiempo real con la webcam, usando YOLOv8n (el modelo mas liviano de [Ultralytics](https://github.com/ultralytics/ultralytics)).

## Requisitos

- Python 3.10+ (probado en 3.14)
- Camara web

## Instalacion

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Uso

Deteccion en vivo (abre una ventana con la camara y las detecciones):

```bash
python webcam_deteccion.py
```

Presiona `q` para salir.

Prueba rapida de un solo frame (util si no tienes entorno grafico):

```bash
python test_camera.py
```

Genera `test_deteccion.jpg` con el resultado.

El modelo `yolov8n.pt` se descarga automaticamente la primera vez que se ejecuta.
