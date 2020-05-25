from playsound import playsound
import os
import time
beep1 = os.path.abspath('beep1.wav')
beep2 = os.path.abspath('beep2.wav')


mors={
    'a':'.- ',
    'b':'-... ',
    'c':'-.-. ',
    'd':'-.. ',
    'e':'. ',
    'f':'..-. ',
    'g':'--. ',
    'h':'.... ',
    'i':'.. ',
    'j':'.--- ',
    'k':'-.- ',
    'l':'.-.. ',
    'm':'-- ',
    'n':'-. ',
    'o':'--- ',
    'p':'.--. ',
    'q':'--.- ',
    'r':'.-. ',
    's':'... ',
    't':'- ',
    'u':'..- ',
    'v':'...- ',
    'w':'.-- ',
    'x':'-..- ',
    'y':'-.-- ',
    'z':'--.. ',
    '1':'.---- ',
    '2':'..--- ',
    '3':'...-- ',
    '4':'....- ',
    '5':'..... ',
    '6':'-.... ',
    '7':'--... ',
    '8':'---.. ',
    '9':'----. ',
    '0':'----- ',
    '.':'.-.-.- ',
    ',':'--..-- ',
    '?':'..--.. ',
    ' ':'/ ',}


while True:
    userInput = input('write something:')
    try:
        for key in userInput:
            morsOutput = mors[key]
            for i in morsOutput:
                if i == '.':
                    playsound(beep1)
                    time.sleep(0.04)
                if i == '-':
                    playsound(beep2)
                    time.sleep(0.05)
            continue
    except KeyError as err:
        print('I dont have this characteer in my dictionary.you can add if yout want.look the code it is easy to understand.')
        continue