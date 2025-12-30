#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 run mypkg talker --ros-args -p work:=0.1 > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep 'Break'
