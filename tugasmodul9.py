import time
import os
from termcolor import colored
text = "Happy Eid"
jarak = 0
arah = 1  
mulai = time.time()
while True:
    os.system('clear')
    spaces = " " * jarak
    print(colored(spaces + text, 'green'))
    time.sleep(0.2)
    if jarak + len(text) >= 50:
        arah = -1
    elif jarak <= 0:
        arah = 1
    jarak += arah
    if time.time() - mulai > 20:
        break