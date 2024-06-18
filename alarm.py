from tkinter import *
import datetime
import time
import pygame
from threading import Thread

# Initialize pygame mixer
pygame.mixer.init()

root = Tk()
root.geometry("400x250")
root.config(bg="#2C0B12")


# Global variables
snooze_active = False
snooze_start_time = None
set_alarm_time = None


def Threading():
    global set_alarm_time
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    global snooze_active, snooze_start_time, set_alarm_time
    while True:
        if set_alarm_time is None:
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time and not snooze_active:
            print("Time to Wake up")
            # Load and play the custom alarm sound with pygame.mixer.Sound
            sound = pygame.mixer.Sound(r"C:\Users\yoges\Downloads\videoplayback (4).mp3")
            sound.play()
            # Wait for the sound to finish playing
            while pygame.mixer.get_busy():
                time.sleep(1)
            # After sound finishes, break out of the loop
            break

        elif current_time == set_alarm_time and snooze_active:
            print("Snooze activated until", (snooze_start_time + datetime.timedelta(minutes=1)).strftime("%H:%M:%S"))
            while datetime.datetime.now() < snooze_start_time + datetime.timedelta(minutes=1):
                time.sleep(1)
            # Reset snooze_active after snooze period
            snooze_active = False
            print("Resuming alarm...")
            # Reset set_alarm_time to trigger the alarm again
            set_alarm_time = None
            continue

        # Check every second
        time.sleep(1)



Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="white",bg="#2C0B12").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold"),bg="#2C0B12",fg="white").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = tuple(f"{i:02}" for i in range(24))
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.config(bg="#c58c85")
hrs["menu"].config(bg="#c58c85", fg="black")
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(60))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.config(bg="#c58c85")
mins["menu"].config(bg="#c58c85", fg="black",activebackground="black")
mins.pack(side=LEFT)
second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(60))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.config(bg="#c58c85",activebackground="#c58c85")
secs["menu"].config(bg="#c58c85", fg="black")
secs.pack(side=LEFT)
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading,bg="#c58c85").pack(pady=20)
root.mainloop()
