import time 
import datetime
import os

alarm_time = input("Enter the time (HH:MM:SS Am/PM): ")


# extract time form the user in time format. 
alarm_hour = alarm_time.split(":")[0]
alarm_minute = alarm_time.split(':')[1]
alarm_second = alarm_time.split(':')[2].split(" ")[0]
period = alarm_time.split(' ')[1].upper()

# convert 12 hour clock into 24 hours clock.
if period == 'PM' and alarm_hour != '12':
    alarm_hour = str(int(alarm_hour) + 12)
elif period == 'AM' and alarm_hour == '12':
    alarm_hour == '00'

# infinite loop for keep checking time. 

while True: 
    now = datetime.datetime.now()

    if now.hour == int(alarm_hour) and now.minute == int(alarm_minute) and now.second == int(alarm_second): 
        print("⏰ Alarm! Time to wake up!")
    
        os.system("start alarm.mp3")  # For Windows: open audio file using default player
        
        break

    time.sleep(1)