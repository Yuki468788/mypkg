#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

# 環境セットアップ
source /opt/ros/humble/setup.bash
source install/setup.bash

# ログをリアルタイムで出力させる
export PYTHONUNBUFFERED=1

# --- 1. 幽霊退治 ---
pkill -f talker || true
pkill -f listener || true

# --- 2. テスト実行 (ここが重要) ---
# launch ファイルを使って一括起動し、出力をすべて /tmp/mypkg.log に保存します。
# 20秒間動かして、終了時のエラーは || true で無視します。
timeout -s SIGINT 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || true

# --- 3. 後始末 ---
pkill -f talker || true
pkill -f listener || true

# --- 4. ログの表示 (GitHub Actionsの画面で確認するため) ---
echo "--- ALL LOG START ---"
cat /tmp/mypkg.log
echo "--- ALL LOG END ---"

# --- 5. 判定 ---
# ログの中に Talker が出した '[timer]: start' または Listener が受信した 'Remaining'
# という文字が 1 つでもあれば、合格 (Exit 0) とします。
grep -E '\[timer\]: start|Remaining' /tmp/mypkg.log
