import keyboard
import time

led = 0
fan = 0

delay = 0.6
last = "0"
lastTime = 0
count = 0

while True:
    isPressed = keyboard.is_pressed("1")
    if isPressed != True:
        t = time.time()
        if count == 1:
            if(t-lastTime >= delay):
                led = 1
        elif count == 2:
            if(t-lastTime >= 2*delay or t-lastTime >= delay):
                led = 0
        elif count == 3:
            if(t-lastTime >= 3*delay or t-lastTime >= 2*delay or t-lastTime >= delay):
                fan = 1
        elif count == 4:
            if(t-lastTime >= 4*delay or t-lastTime >= 3*delay or t-lastTime >= 2*delay or t-lastTime >= delay):
                fan = 0
        last = isPressed
    else:
        t = time.time()
        if last != isPressed:
            last = isPressed
            if t - lastTime > delay:
                count = 1
            else:
                count += 1
            if count >= 5:
                count = 0
            lastTime = t