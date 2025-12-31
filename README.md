# ポモドーロタイマー
[![test](https://github.com/Yuki468788/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Yuki468788/mypkg/actions/workflows/test.yml)
このパッケージはtalkerから配信される時間をもとにlistener,guiで残り時間を取得することができ、25分作業、5分休憩のサイクルを繰り返す

## 実行方法
- 以下のコマンドで実行可能
```
$ ros2 launch mypkg talk_listen.launch.py
[talker-1] [INFO] [1767158197.464888484] [timer]: start
[listener-2] [INFO] [1767158198.474950393] [listener]: [UNKNOWN] | Remaining:24:59
[listener-2] [INFO] [1767158199.460223700] [listener]: [UNKNOWN] | Remaining:24:58
[listener-2] [INFO] [1767158200.459827484] [listener]: [UNKNOWN] | Remaining:24:57
[listener-2] [INFO] [1767158201.459292362] [listener]: [UNKNOWN] | Remaining:24:56
[listener-2] [INFO] [1767158202.458988685] [listener]: [UNKNOWN] | Remaining:24:55
[listener-2] [INFO] [1767158203.459133100] [listener]: [UNKNOWN] | Remaining:24:54
[listener-2] [INFO] [1767158204.459547583] [listener]: [UNKNOWN] | Remaining:24:53
[listener-2] [INFO] [1767158205.459011927] [listener]: [UNKNOWN] | Remaining:24:52
[listener-2] [INFO] [1767158206.459598244] [listener]: [UNKNOWN] | Remaining:24:51
[listener-2] [INFO] [1767158207.459271269] [listener]: [UNKNOWN] | Remaining:24:50
[listener-2] [INFO] [1767158208.459139965] [listener]: [UNKNOWN] | Remaining:24:49
[listener-2] [INFO] [1767158209.459367884] [listener]: [UNKNOWN] | Remaining:24:48
[listener-2] [INFO] [1767158210.459600364] [listener]: [UNKNOWN] | Remaining:24:47
[listener-2] [INFO] [1767158211.459444648] [listener]: [UNKNOWN] | Remaining:24:46
[listener-2] [INFO] [1767158212.458959531] [listener]: [UNKNOWN] | Remaining:24:45
[listener-2] [INFO] [1767158213.459261407] [listener]: [UNKNOWN] | Remaining:24:44
[listener-2] [INFO] [1767158214.459443257] [listener]: [UNKNOWN] | Remaining:24:43
[listener-2] [INFO] [1767158215.460347455] [listener]: [UNKNOWN] | Remaining:24:42
[listener-2] [INFO] [1767158216.459713242] [listener]: [UNKNOWN] | Remaining:24:41
[listener-2] [INFO] [1767158217.460185296] [listener]: [UNKNOWN] | Remaining:24:40
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
- 参照したコード
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Yuki Akutsu

