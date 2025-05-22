import datetime
import time
import tkinter as tk
from threading import Thread
import os

def check_alarm():
    while True:
     
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

       
        if current_time == alarm_time_24.get():
            status_label.config(text="⏰ Wake up! Alarm ringing!")
            os.system("start alarm.mp3")
            break
        time.sleep(1)


def set_alarm():
    hr = hour.get()
    mn = minute.get()
    sec = second.get()
    am_pm = period.get()

   
    if am_pm == "PM" and hr != "12":
        hr = str(int(hr) + 12)
    elif am_pm == "AM" and hr == "12":
        hr = "00"

    
    alarm_time_24.set(f"{hr.zfill(2)}:{mn.zfill(2)}:{sec.zfill(2)}")
    status_label.config(text=f"✅ Alarm set for {alarm_time_24.get()}")

   
    t = Thread(target=check_alarm)
    t.start()


app = tk.Tk()
app.title("Alarm Clock")
app.geometry("300x250")
app.config(bg="lightblue")


hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()
period = tk.StringVar(value="AM")
alarm_time_24 = tk.StringVar()


tk.Label(app, text="Set Alarm Time", font=("Helvetica", 16), bg="lightblue").pack(pady=10)


frame = tk.Frame(app, bg="lightblue")
frame.pack()

tk.Entry(frame, textvariable=hour, width=3).pack(side=tk.LEFT)
tk.Label(frame, text=":", bg="lightblue").pack(side=tk.LEFT)

tk.Entry(frame, textvariable=minute, width=3).pack(side=tk.LEFT)
tk.Label(frame, text=":", bg="lightblue").pack(side=tk.LEFT)

tk.Entry(frame, textvariable=second, width=3).pack(side=tk.LEFT)


tk.OptionMenu(frame, period, "AM", "PM").pack(side=tk.LEFT, padx=5)


tk.Button(app, text="Set Alarm", command=set_alarm).pack(pady=10)


status_label = tk.Label(app, text="", bg="lightblue", fg="green", font=("Helvetica", 12))
status_label.pack(pady=5)


app.mainloop()
