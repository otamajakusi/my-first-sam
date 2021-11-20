import cv2
import torch
import torchvision
import boto3


def detect(weights):
    net = cv2.dnn.readNetFromONNX(weights)
    s3 = boto3.client("s3", endpoint_url="http://localstack:4566")
    s3.upload_file(
        "yolov5s.onnx",
        "weights",
        "yolov5s.onnx",
    )
