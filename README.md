# Real-time-detection-tool
PCの画面上で物体検知を行い、リアルタイムでディスプレイに反映するための補助ツール  



https://github.com/user-attachments/assets/e919435f-a926-49d9-bbe4-bbf91eabf268


# 特徴
・リアルタイム検出: 定期的にスクリーンショットを取得し、YOLOv5で物体を検出します。  
・オーバーレイ表示: 画面上で検出結果にバウンディングボックスとクラスラベルを表示します。  
・カスタムモデル対応: ローカルで学習させたYOLOv5モデルを読み込み、特定の物体を検出できます。  
・ユーザー操作で終了: Q キーを押してシステムを終了可能です。

# 必要環境
・Python 3.8以降  
・ハードウェア：CPUもしくはGPU搭載のシステムが推奨  
・必要なPythonライブラリ：
```
mss
pillow
torch
pandas
tkinter
```
# インストール
1.リポジトリをクローンします:
```bash
git clone https://github.com/Snow2Shoe/Real-time-detection-tool.git
cd your-repo
```

2.必要なPythonパッケージをインストールします:
```bash
pip install -r requirements.txt
```

3.YOLOv5モデルをダウンロードします:  
学習済みのYOLOモデル（例：`yolov5s.pt`）を配置し、`main.py`にてパスを指定してください。

# 使い方
1.`main.py`でYOLOモデルのパスを更新します:
```bash
yolo_repo_path = "path/to/yolov5"
model_path = "path/to/your/yolov5s.pt"
```

2.システムを実行します:
```bash
python main.py
```
3.オーバーレイウィンドウが表示されている状態でQキーを押すと、プログラムを終了できます。

# 設定
・モニターインデックス: デフォルトではプライマリモニターを使用しますが、他のモニターを指定する場合は`run_yolo_detection`内の`monitor_index`を変更してください。  
・信頼度の閾値: 検出感度を調整するには、`run_yolo_detection`内の`confidence_threshold`を変更してください。  

# 仕組み
1.スクリーンキャプチャ: `screenshot_utils.py`では`mss`を用いてスクリーンショットを取得します。  
2.YOLOによる検出: `yolo_detection.py`でYOLOv5モデルを読み込み、スクリーンショットを処理して物体を検出します。  
3.オーバーレイ表示: `display_results.py`でTkinterウィンドウを用いて、検出された物体にバウンディングボックスやクラスラベルをオーバーレイ表示します。

# 注意
実行時に`hubconf.py`でエラーが発生した場合は`hubconf.py`内のコードを以下のように修正して、再度実行してください。  

`hubconf.py` line 52  
- 修正前  
```bash
    from pathlib import Path
```
- 修正後  
```bash
    import pathlib
    from pathlib import Path

    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
```
