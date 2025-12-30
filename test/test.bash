#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source /opt/ros/humble/setup.bash
source install/setup.bash

# ログ出力の遅延を防ぐ設定
export PYTHONUNBUFFERED=1

# テスト実行（30秒間動かす）
# エラー出力も含めてログ保存 (2>&1)
timeout -s SIGINT 30 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

# 画面にログを出して確認用
cat /tmp/mypkg.log

# 【ここがポイント】
# "Listen" という文字さえログにあれば、数字が何であれ通信成功とみなす！
cat /tmp/mypkg.log | grep 'Listen'
