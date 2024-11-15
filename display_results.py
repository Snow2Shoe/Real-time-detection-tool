import tkinter
import time

def initialize_display_window(terminate_event):
    root = tkinter.Tk()
    root.wm_attributes("-transparentcolor", "snow")
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    canvas = tkinter.Canvas(root, width=screen_width, height=screen_height, bg="snow")
    canvas.place(x=0, y=0)

    # 「Q」キーで終了フラグをセット
    root.bind("<KeyPress-q>", lambda event: terminate_event.set())
    
    return root, canvas

def display_detected_objects(queue, terminate_event):
    root, canvas = initialize_display_window(terminate_event)
    
    while not terminate_event.is_set():  # フラグが立つまでループ
        root.update()
        
        if not queue.empty():
            detection_results = queue.get()
            for result in detection_results:
                x1, y1, x2, y2, confidence, class_name = result[0], result[1], result[2], result[3], result[4], result[6]
                rectangle = canvas.create_rectangle(x1, y1, x2, y2, tags='object', outline="red", width=3)
                canvas.create_text(x1-20, y1-20, text=f"{class_name}:{str(confidence)[:4]}", font=('MS Gothic', 20, "bold"), fill="red", tags='object')
            
            canvas.pack()
            canvas.update()
            canvas.delete('object')
        
        time.sleep(0.1)
    
    root.destroy()