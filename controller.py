from pynput import keyboard

def count_experience():
    count = 0
    while True:
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.esc:
                    break
                elif (str(event)) == "Press(key='1')":
                        c+=1
                        print(count) 


count_experience()