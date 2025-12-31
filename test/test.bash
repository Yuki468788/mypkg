#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source /opt/ros/humble/setup.bash
source install/setup.bash
export PYTHONUNBUFFERED=1

export DISPLAY=:99
Xvfb :99 -screen 0 1024x768x24 &
sleep 2
pkill -f talker || true
pkill -f listener || true
pkill -f gui || true
timeout -s SIGINT 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || true

pkill -f talker || true
pkill -f listener || true
pkill -f gui || true
echo "--- ALL LOG START ---"
cat /tmp/mypkg.log
echo "--- ALL LOG END ---"

grep '\[timer\]: start' /tmp/mypkg.log && \
grep 'Remaining' /tmp/mypkg.log && \
grep 'gui-' /tmp/mypkg.log
