Overview

This project implements a real-time road anomaly detection system using a lightweight YOLO-based deep learning model. The model was trained in PyTorch and exported to ONNX format for efficient and portable inference on edge devices.

The system processes dashcam video frames and detects road anomalies such as potholes and surface damage in real time. The objective is to enable low-latency detection suitable for embedded and edge deployment environments.

Problem Statement

Road surface anomalies such as potholes significantly impact vehicle safety, maintenance cost, and ride quality. Traditional manual inspection is slow, inconsistent, and expensive.

This project provides an automated vision-based detection pipeline capable of:

Detecting road anomalies from video streams

Operating in real time

Supporting edge deployment using ONNX runtime

System Architecture
Dashcam Video Input
        ↓
Frame Extraction
        ↓
Preprocessing
        ↓
YOLO Model (PyTorch)
        ↓
Model Export (.pt → .onnx)
        ↓
ONNX Runtime Inference
        ↓
Bounding Box Detection Output
Methodology

Data collection and preprocessing

Model training using PyTorch

Performance evaluation using validation dataset

Export trained model from .pt to .onnx

Real-time inference using ONNX Runtime

Performance optimization for edge deployment

Model Details

Framework: PyTorch

Export Format: ONNX

Model Type: Lightweight YOLO variant

Input: RGB video frames

Output: Bounding boxes with confidence scores

Inference Engine: ONNX Runtime

Applications :

Smart transportation systems
Road condition monitoring
Autonomous vehicle assistance
Predictive infrastructure maintenance
