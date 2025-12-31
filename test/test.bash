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

# --- 1. 念のため古いプロセスを掃除 ---
pkill -f talker || true

# --- 2. Talkerをバックグラウンドで起動 ---
# パラメータで時間を短く(0.1分)設定
ros2 run mypkg talker --ros-args -p work:=0.1 &
TALKER_PID=$!

# 起動を少し待つ
sleep 5

# --- 3. 1回だけデータを受信して保存 ---
# --once があるので、1つでもデータを受け取ればこのコマンドは即終了します
# 万が一データが届かない時のために timeout 15 をつけています
timeout 15 ros2 topic echo --once /timer_state > /tmp/echo.log || true

# --- 4. 後始末 ---
kill $TALKER_PID || true
pkill -f talker || true

# --- 5. 判定 ---
# ログを表示
cat /tmp/echo.log

# ログの中に "data:" という文字列があれば、通信成立とみなして合格(Exit 0)
grep 'data:' /tmp/echo.log
