# **Python Timer with Sound Notification**  

This program is a **Python-based countdown timer** that plays an alert sound when the timer reaches the last 5 seconds and again when it ends. It utilizes **multithreading** to ensure the sound plays without interrupting the countdown. The script also features **dynamic console updates** to display the remaining time in a clear and visually appealing format.

---

## **Features**  

### ✅ **Customizable Timer**  
- The user inputs the desired **minutes** and **seconds**, and the timer starts accordingly.  

### ✅ **Real-time Countdown Display**  
- The remaining time updates dynamically in the console, formatted as **MM:SS**.  
- Uses **ANSI escape codes** (`\033[H`) to clear and refresh the display for a smooth countdown experience.  

### ✅ **Sound Alerts**  
- **First alert**: A sound plays **5 seconds before** the timer reaches zero.  
- **Final alert**: A sound plays **once the timer ends**.  
- Uses `playsound` to play an external MP3 file (`Sound.mp3`).  

### ✅ **Multithreading for Non-Blocking Sound Playback**  
- The sound function runs in a **separate thread**, ensuring it doesn't freeze the timer while playing.  
- If the sound is already playing when the timer ends, the script **waits for it to finish** before playing the final alert.  


## **Why Use Multithreading?**  
- Without **threads**, the program would **freeze** while playing the sound.  
- With **threads**, the timer continues updating smoothly even when the sound plays.  

---

## **Requirements**  
- **Python** (Latest version recommended)  
- **Playsound Library** (Install using `pip install playsound`)  
- **An MP3 file** named `"Sound.mp3"` in the project directory  

---

## **Future Enhancements**  
✅ Add **GUI Support** using **Tkinter or PyQt**  
✅ Allow users to choose **custom sounds**  
✅ Implement a **pause & resume** feature  

---

