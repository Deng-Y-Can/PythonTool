import tkinter as tk
import time
import threading


def hide_window():
    root.iconify()


def show_window():
    root.deiconify()
    root.attributes("-topmost", 1)  # 设置窗口置顶
    root.geometry(
        "+%d+%d"
        % (
            (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2,
            (root.winfo_screenheight() - root.winfo_reqheight()) / 2,
        )
    )
    root.after(1000, lambda: root.attributes("-topmost", 0))  # 1秒后取消置顶


def start_timer(second):
    time.sleep(second)
    show_window()


def blink_window():
    for _ in range(4):  # 闪烁两次
        root.attributes("-alpha", 0)  # 隐藏窗口
        root.update()
        time.sleep(0.5)  # 0.5秒延迟
        root.attributes("-alpha", 1)  # 显示窗口
        root.update()
        time.sleep(0.5)  # 0.5秒延迟


def on_start_button_click():
    hide_window()
    minutes = int(entry.get())
    threading.Thread(target=start_timer, args=(minutes,), daemon=True).start()
    threading.Thread(target=blink_window, daemon=True).start()


# 创建主窗口
root = tk.Tk()
root.title("休息提醒")

# 创建标签和输入框
label = tk.Label(root, text="输入休息时长（秒）:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# 创建开始按钮
start_button = tk.Button(root, text="开始", command=on_start_button_click)
start_button.pack(pady=20)

# 设置窗口大小
root.geometry("300x150")

# 运行主循环
root.mainloop()