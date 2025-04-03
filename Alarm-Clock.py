import time
import winsound

alarm_time = input("Enter the time for the alarm (HH:MM): ")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("WAKE UP!")
        winsound.Beep(1000, 2000)
        break
    time.sleep(30)
