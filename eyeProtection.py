import threading
import keyboard
import pygame
import time

def play_mp3():
    pygame.mixer.init()
    pygame.mixer.music.load("look_around.mp3")
    pygame.mixer.music.play()

def stop_mp3():
    keyboard.wait("shift+L")
    pygame.mixer.music.stop()

def timer():
    time.sleep(20 * 60)  # Wait for 20 minutes
    keyboard.press_and_release('shift+L')  # Simulate 'Shift+L' key press to stop playback

if __name__ == "__main__":
    mp3_thread = threading.Thread(target=play_mp3)
    stop_thread = threading.Thread(target=stop_mp3)
    timer_thread = threading.Thread(target=timer)

    mp3_thread.start()
    timer_thread.start()
    stop_thread.start()

    mp3_thread.join()
    timer_thread.join()
    stop_thread.join()
