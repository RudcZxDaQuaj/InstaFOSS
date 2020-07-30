from pushbullet import Pushbullet
def read():
    f = open('pushbullet', 'r')
    pb = Pushbullet(f.read(34))

def donenotif():
    f = open('pushbullet', 'r')
    pb = Pushbullet(f.read(34))
    push = pb.push_note('InstagramBot: Done!', 'It is recommended to check the Python Shell for more info')
