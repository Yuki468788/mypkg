# ポモドーロタイマー

このパッケージはtalkerから取得した時間をもとにlistener,guiで残り時間を取得することができ、25分作業、5分休憩のサイクルを続ける

## 実行方法
- 以下のコマンドで実行可能
```
$ ros2 launch mypkg talk_listen.launch.py

```
## ノード説明
### talker
- WORKとBRAKEのステータスを取得し、そのステータスにあったタイマーを取得
### listener
- talkerが取得している残り時間をlistenerで受信する
### gui
- talkerが取得している時間をTkinterで視覚化する
## テスト環境
- Ubuntu 22.04.5 LTS
- Python 3.10
## 謝辞
- 参照したコード
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Yuki Akutsu

