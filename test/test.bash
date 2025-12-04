#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmo/mypkg.log
grep 'listen: 10'
