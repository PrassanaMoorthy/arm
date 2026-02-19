import cv2
from ultralytics import YOLO

model = YOLO(
    r"D:\New folder\mod\best_model.onnx",
    task="detect"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(
        frame,
        imgsz=640,
        conf=0.45,  
        iou=0.5, 
        agnostic_nms=True,
        max_det=100,
        verbose=False
    )

    annotated = results[0].plot()
    cv2.imshow("YOLO ONNX", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()