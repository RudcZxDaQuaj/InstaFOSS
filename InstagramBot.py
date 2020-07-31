#InstaFOSS (Python edition : GitHub release!!) version: 2.0
# ---------------------------------------------------------------------------
# I understand this entire thing is probably incredibly messy but this is
# quite literally my second python project, unless you consider "Hello World"
# to not be a project then this would be my first. If there's a bug feel free
# to report it or make a fork to fix it yourself.
#
# Also this was written by one guy on GitHub as a FOSS project, FOSS being
# "Free and Open Source Software", if you see anyone monetizing off this code
# or making you pay to use it, they're scamming you and you're likely using
# an outdated version. There's a weird amount of people charging outrageous
# monthly subscriptions to boost instagram accounts using likes and scripts
# like these but mine aims to be more efficent and most importantly free.
# ---------------------------------------------------------------------------

import random
import time
import pyautogui
#custom modules
import config
from pushbullet import Pushbullet
from instapushbullet import read, donenotif
if(config.pushbulletnotif == True):
    read()

pyautogui.PAUSE = 0.5
pyautogui.failsafe = True

print('Enter the amount of likes you wanna hand out')
useramount = int(input())
# I know it's bad practice to initalize variables at the top especially before they're used, but
# I'm fairly new to python and I can't figure out a better way to do this, if you have a better
# way please lemme know.
totalamount = 0
skipnumber = 0
slowloadingpost = 0

while useramount > 0:
    skiptime = random.randrange(0, 1)
    totalamount+=1
    los = random.randint(0, 3)
    s = pyautogui.locateOnScreen('actionblock.png')
    if(s != None):
        push = pb.push_note('InstagramBot: ActionBlock!', 'Please check Python Shell for more info')
        print('--------ACTION BLOCKED--------')
        print('Sorry for the inconvience, an action block on instagram')
        print('just means that you probably entered too many likes, the')
        print('average limit for actions on instagram is 1440 in 24')
        print('hours, a temporary solution to this would be clearing')
        print('clearing your browser cache for instagram and logging')
        print('back in--It is recommended to only do around 500-700 likes')
        print('per day, although this number would vary based on your')
        print('daily activity.')
        print(' ')
        print('If there was no action block and this block was a false')
        print('positive please let the developers know...')
        print('--------ACTION BLOCKED--------')
        print(' ')
        input('Enter any key to exit...')
        exit()
    mox, moy = pyautogui.position()
    pixel = pyautogui.screenshot(
        region=(
            mox, moy, 1, 1
        )
    )
    if(los == 0):
        #skipping
        time.sleep(50 / 100)
        pyautogui.press('right')
        skipnumber+=1
        time.sleep(skiptime)
        print('skipped... took ' + str(int(skiptime)) + ' seconds to skip')
    else:
        #liking
        time.sleep(50 / 1000)
        randsleepbtlike = random.randrange(0, 1)
        pyautogui.moveTo(config.mx, config.my, duration=0.15)
        time.sleep(randsleepbtlike)
        mox, moy = pyautogui.position()
        pixel = pyautogui.screenshot(
            region=(
               mox, moy, 1, 1,
            )
        )
        time.sleep(1 / 500)
        color = pixel.getcolors()
        while(color == [(1, (239, 239, 239))]):
            pyautogui.press('right')
            print('slow loading post detected...')
            time.sleep(2)
            pyautogui.moveTo(config.mx, config.my, 0.25)
            time.sleep(randsleepbtlike)
            slowloadingpost+=1
            mox, moy = pyautogui.position()
            pixel = pyautogui.screenshot(
                region=(
                   mox, moy, 1, 1,
                )
            )
            color = pixel.getcolors()
            if(slowloadingpost == 3):
                print('(slow loading checks are not always accurate, probably more posts did not load! Please keep that in mind.)')
                print('----------------------')
                print('Roughly 5 slow loading posts detected, interrupting script as this poses a danger to your account being action blocked.')
                print('Waiting 2:45 minutes before continuing...')
                print('----------------------')
                time.sleep(60)
                pyautogui.press('right')
                time.sleep(60)
                pyautogui.press('right')
                time.sleep(35)
                slowloadingpost = 0
                time.sleep(5)
                mox, moy = pyautogui.position()
                pixel = pyautogui.screenshot(
                    region=(
                       mox, moy, 1, 1,
                    )
                )
                color = pixel.getcolors()
                if(color == [(1, (239, 239, 239))]):
                    print('Sorry for the inconvience, slow loading posts are popping up often')
                    break
                else:
                    print('Slow loading posts fixed... Continuing')
                    break
        pyautogui.click(config.mx, config.my, clicks=2)
        useramount = (useramount - 1)
        print('liked... ' + str(int(useramount)) + ' posts left to go!')
        time.sleep(1 / 2) 
        pyautogui.press('right')
        slowloadingpost = 0
    if(useramount == 0):
        #finish
        if(config.pushbulletnotif == True):
            donenotif()
        print('Done! total was ' + str(int(totalamount)) + ' posts seen! ' + str(int(skipnumber)) + ' posts skipped')
