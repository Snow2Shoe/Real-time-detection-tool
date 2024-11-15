import time
from multiprocessing import Queue, Process, Event
from yolo_detection import load_yolo_model, run_yolo_detection
from display_results import display_detected_objects

def detection_process(queue, terminate_event, yolo_repo_path, model_path):
    # YOLOモデルのロード
    try:
        model = load_yolo_model(yolo_repo_path, model_path)
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        return

    while not terminate_event.is_set():  # 終了フラグを監視
        try:
            results = run_yolo_detection(model, monitor_index=0)
            queue.put(results)
        except Exception as e:
            print(f"Error in YOLO detection: {e}")
            break

def main():
    # 結果キューと終了イベント
    detection_queue = Queue()
    terminate_event = Event()
    
    # YOLOモデルのパス
    yolo_repo_path = "yolov5ディレクトリのパス"
    model_path = "使用するモデルのパス"
    
    # プロセスの作成
    detection_proc = Process(target=detection_process, args=(detection_queue, terminate_event, yolo_repo_path, model_path))
    display_proc = Process(target=display_detected_objects, args=(detection_queue, terminate_event))
    
    detection_proc.start()
    display_proc.start()
    
    # 終了フラグが立つまでプロセスを監視
    display_proc.join()
    
    # 終了フラグを立ててYOLOプロセスも終了
    terminate_event.set()
    detection_proc.join()

if __name__ == '__main__':
    main()