import torch
import pandas as pd
from screenshot_utils import capture_screenshot

# YOLOv5のカスタムモデルをローカルリポジトリからロード
def load_yolo_model(yolo_repo_path, model_path):
    device = torch.device("cpu")
    model = torch.hub.load(yolo_repo_path, 'custom', path=model_path, source='local').to(device)
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
