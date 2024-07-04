import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style


Worktime = 25 * 60
Shorttime = 5 * 60
Longtime = 15 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        self.style = Style("simplex")
        self.style.theme_use()
        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="START", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="STOP", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.brake_time = Worktime, Shorttime
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()


    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            self.work_time -= 1
            if self.work_time == 0:
                self.is_work_time = False
                self.pomodoros_completed += 1
                self.brake_time = Longtime if self.pomodoros_completed % 4 == 0 else Shorttime
                messagebox.showinfo("Great Job!"if self.pomodoros_completed% 4 == 0
                                else "Good Job, take a long break and chill out"
                                if self.pomodoros_completed % 4 == 0
                                else "take a short break and stretch a bit")
            
        else:
            self.brake_time -= 1
            if self.brake_time == 0:
                self.is_work_time, self.work_time = True, Worktime
                messagebox.showinfo("Worktime!! Get to it!", "Get back to Work!")
        minutes, seconds = divmod(self.work_time if self.is_work_time else self.brake_time, 60)
        self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
        self.root.after(1000, self.update_timer)


PomodoroTimer()
