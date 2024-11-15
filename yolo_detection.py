import torch
import pandas as pd
from screenshot_utils import capture_screenshot

# YOLOモデルの初期化
def load_yolo_model(model_path, device="cpu"):
    device = torch.device(device)
    model = torch.hub.load('C:/Users/Greek/yolov5', 'custom', path=model_path, source='local').to(device)
    return model

def run_yolo_detection(model, monitor_index=0, confidence_threshold=0.4):
    image = capture_screenshot(monitor_index)
    results = model(image)
    return filter_results(results, confidence_threshold)

def filter_results(results, confidence_threshold):
    result_dataframe = results.pandas().xyxy[0]
    result_dataframe.iloc[:, :4] = result_dataframe.iloc[:, :4].astype('int')
    filtered_results = result_dataframe[result_dataframe['confidence'] >= confidence_threshold]
    return filtered_results.values.tolist()