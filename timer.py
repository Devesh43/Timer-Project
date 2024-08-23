from playsound import playsound
import time

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

def timer(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed  < seconds:
        time.sleep(1)
        time_elapsed +=1

        time_left =  seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Timer will end in : {minutes_left:02d}:{seconds_left:02d}")

    playsound("Sound.mp3")

minutes = int(input("How many minutes till the timer goes off? : "))
seconds = int(input("How many seconds till the timer goes off? : "))
total_seconds = minutes * 60 + seconds
timer(total_seconds)


