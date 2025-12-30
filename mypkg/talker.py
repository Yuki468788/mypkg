#!/usr/bin/python
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 , String

class Timer(Node):
    def __init__(self):
        super().__init__('timer')

        self.declare_parameter('work' , 25.0)
        self.declare_parameter('break' , 5.0)

        self.work_min = self.get_parameter('work').value
        self.break_min = self.get_parameter('break').value

        self.pub_state = self.create_publisher(String, 'timer_state' , 10)
        self.pub_time = self.create_publisher(Int16, 'remaining_seconds' , 10)

        self.state = "WORK"
        self.remaining_sec = int(self.work_min * 60)

        self.create_timer(1.0, self.callback)
        self.get_logger().info(f"start")

    def callback(self):

        self.remaining_sec -= 1

        if self.remaining_sec < 0:
            if self.state == "WORK":
                self.state = "BREAK"
                self.remaining_sec = int(self.break_min * 60)
                self.get_logger().info("Break")
            else:
                self.state = "WORK"
                self.remaining_sec = int(self.work_min * 60)
                self.get_logger().info("Restart")

        msg_time = Int16()
        msg_time.data = self.remaining_sec
        self.pub_time.publish(msg_time)

def main():
    rclpy.init()
    node = Timer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()
