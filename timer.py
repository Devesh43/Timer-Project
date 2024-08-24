from playsound import playsound
import time
import threading

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

def play_sound():
    playsound("Sound.mp3")

def timer(seconds):
    time_elapsed = 0
    sound_thread = None

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        if time_left > 0:
            print(f"{CLEAR_AND_RETURN}Timer will end in : {minutes_left:02d}:{seconds_left:02d}", end="\r")
        
        if time_left == 5:
            sound_thread = threading.Thread(target=play_sound)
            sound_thread.start()

    
    print(CLEAR_AND_RETURN + "Timer ended!" + " " * 20) 

    
    if sound_thread and sound_thread.is_alive():
        sound_thread.join(timeout=6)
    
    else:
        sound_thread = threading.Thread(target=play_sound)
        sound_thread.start()
        time.sleep(6)
        sound_thread.join()

minutes = int(input("How many minutes till the timer goes off? : "))
seconds = int(input("How many seconds till the timer goes off? : "))
total_seconds = minutes * 60 + seconds
timer(total_seconds)
