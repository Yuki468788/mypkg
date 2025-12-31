# ポモドーロタイマー
[![test](https://github.com/Yuki468788/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Yuki468788/mypkg/actions/workflows/test.yml)

このパッケージはtalkerから配信される時間をもとにlistener,guiで残り時間を取得することができ、25分作業、5分休憩のサイクルを繰り返す

## 実行方法
- 以下のコマンドで実行可能
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/yuki/.ros/log/2025-12-31-14-16-37-179604-TpR-28732
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [28735]
[INFO] [listener-2]: process started with pid [28737]
[INFO] [gui-3]: process started with pid [28739]
[talker-1] [INFO] [1767158197.464888484] [timer]: start
[listener-2] [INFO] [1767158198.474950393] [listener]: [UNKNOWN] | Remaining:24:59
[listener-2] [INFO] [1767158199.460223700] [listener]: [UNKNOWN] | Remaining:24:58
[listener-2] [INFO] [1767158200.459827484] [listener]: [UNKNOWN] | Remaining:24:57
```
## ノード説明
### talker
- WORKとBREAKのステータスを管理し、そのステータスにあったタイマーの情報を配信する
### listener
- talkerが取得している残り時間をlistenerで受信し、ターミナルで表示する
### gui
- talkerが取得している時間をquiで受信し、デスクトップ上で可視化する
## テスト環境
- Ubuntu 22.04.5 LTS
- ROS2 Humble
- Python 3.10
## 謝辞
- 参考にした資料・サイト
- [tkinter 使い方のまとめ（基本編）](https://qiita.com/omossan7182t/items/ccc95de88a079596bf7a)
- 参照したコード
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
## 著作権
- © 2025 Yuki Akutsu

