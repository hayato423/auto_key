import time
import pyautogui as pg
time_start = time.time()
print('Running auto_key')
while True:
    time_end = time.time()
    if time_end - time_start > 300:
        pg.keyDown('ctrl')
        pg.keyUp('ctrl')
        time_start = time.time()
