import time

def p_delay(message,delay=1):
    print(message)
    time.sleep(delay)

p_delay("This message prints and adds a 3 second delay till the next print statement",3)