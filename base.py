import time
import winsound

def play_sound():
    # Play a sound (you can change the filename or path to your desired sound file)
    winsound.PlaySound("look_around.mp3", winsound.SND_FILENAME)

# Set the time interval in seconds (20 minutes = 20 * 60 seco
interval = 20 * 60

while True:
    play_sound()
    time.sleep(interval)
