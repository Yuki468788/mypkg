#!/usr/bin/python
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16
import tkinter as tk

class PomodoroGUI(Node):
    def __init__(self, root):
        super().__init__('pomodoro_gui')
        self.root = root
        
        # --- ウィンドウ設定 ---
        self.root.title("ROS 2 Focus Timer")
        self.root.geometry("400x250") 
        self.root.resizable(False, False) 
        self.root.attributes('-topmost', True)

        self.COLORS = {
            "bg": "#212121",       # 背景: ダークグレー
            "text": "#E0E0E0",     # 基本文字: オフホワイト
            "work": "#FF5252",     # 作業色: ネオンレッド
            "break": "#69F0AE",    # 休憩色: ネオングリーン
            "stop":  "#9E9E9E"     # 停止中: グレー
        }

        # 背景色の適用
        self.root.configure(bg=self.COLORS["bg"])

        # --- GUIパーツ配置 ---
        # 1. ヘッダー (状態表示)
        self.lbl_status = tk.Label(
            root, 
            text="WAITING...", 
            font=("Helvetica", 14, "bold"),
            bg=self.COLORS["bg"], 
            fg=self.COLORS["stop"]
        )
        self.lbl_status.pack(pady=(30, 0))

        # 2. メインタイマー表示
        self.lbl_time = tk.Label(
            root, 
            text="00:00", 
            font=("Helvetica", 70, "bold"), 
            bg=self.COLORS["bg"], 
            fg=self.COLORS["text"]
        )
        self.lbl_time.pack(pady=0)

        # 3. フッター (メッセージ)
        self.lbl_message = tk.Label(
            root,
            text="Waiting for ROS 2 topic...",
            font=("Helvetica", 10),
            bg=self.COLORS["bg"],
            fg=self.COLORS["text"]
        )
        self.lbl_message.pack(side=tk.BOTTOM, pady=20)

        # --- ROS 2 Subscriber ---
        self.create_subscription(String, 'timer_state', self.cb_state, 10)
        self.create_subscription(Int16, 'remaining_seconds', self.cb_time, 10)
        
        # 内部変数
        self.current_state = "STOP"

    def cb_state(self, msg):
        state = msg.data
        self.current_state = state
        
        if state == "WORK":
            display_text = "FOCUS TIME"
            color = self.COLORS["work"]
        elif state == "BREAK":
            display_text = "BREAK TIME"
            color = self.COLORS["break"]
        else:
            display_text = state
            color = self.COLORS["stop"]
            msg_text = "---"

        # GUIへの反映
        self.lbl_status.config(text=display_text, fg=color)
        self.lbl_time.config(fg=color) 
        self.lbl_message.config(text=msg_text)

    def cb_time(self, msg):
        seconds = msg.data
        mins = seconds // 60
        secs = seconds % 60
        self.lbl_time.config(text=f"{mins:02d}:{secs:02d}")

    def update_gui(self):
        """ROS 2の処理を定期的に呼び出す"""
        rclpy.spin_once(self, timeout_sec=0)
        self.root.after(100, self.update_gui)

def main():
    rclpy.init()
    root = tk.Tk()
    node = PomodoroGUI(root)
    node.update_gui()
    root.mainloop()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
