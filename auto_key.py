from time import sleep
import pyautogui as pg
start_pos = pg.position()
print('Running auto_key')
while True:
    sleep(300)
    end_pos = pg.position()
    if start_pos == end_pos:
        pg.keyDown('ctrl')
        pg.keyUp('ctrl')
        print('Push ctrl Key!')
    else:
        start_pos = pg.position()
