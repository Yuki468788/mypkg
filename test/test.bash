#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

if [ -f $dir/.bashrc ]; then
    source $dir/.bashrc
else
    source /opt/ros/humble/setup.bash
fi
source install/setup.bash
ros2 run mypkg talker --ros-args -p work:=0.1 &
TALKER_PID=$!
sleep 2
timeout 15 ros2 run mypkg listener > /tmp/mypkg.log 2>&1

kill $TALKER_PID
cat /tmp/mypkg.log | grep 'Break'
