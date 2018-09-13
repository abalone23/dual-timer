# Add your Python code here. E.g.
from microbit import *

# 12 clock images
# 30 sec = 2.5 per per image
# 60 sec = 5 sec per image

while True:
    if button_a.is_pressed():
        timer_delay = 2500
        break
    elif button_b.is_pressed():
        timer_delay = 5000
        break

display.show(Image.ALL_CLOCKS, loop=False, delay=timer_delay)
display.show(Image.HAPPY)
sleep(10000)
display.clear()
reset()