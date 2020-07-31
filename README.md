# InstaFOSS

InstaFOSS is one of my first python projects, it utilizes PyAutoGui and Pushbullet to automatically like posts on Instagram 
with human like reaction times, color recognition for when a post isn't loading properly, image recognition to detect
action blocks and status updates to your phone or other devices using Pushbullets API.

The goal is to mass like specific hashtags so people get notifications leading you to your account, gaining more attention,
this works pretty well when doing 500-600 likes, but pushing it too far could get you an action block.

I've tested this program in my own time and with sparse usage (usually only 2 days a week) over the past couple of months it 
has gotten roughly 400 followers. With daily usage on the right hashtags it could earn maybe 1000 over the course of a month,
ofcourse this isn't the best way to gain followers, but running it in the background on a seperate device does help a lot for smaller 
accounts.

## Getting started:
### Requirements:
* Latest version of python
* PyAutoGui
* Pushbullet
if you don't wanna install PyAutoGui and Pushbullet manually just go to the main directory and enter
  >pip install -r requirements.txt

this will automatically install all required python libraries.

### Actually running the thing
* Open a perferred hashtag you want likes or followers from.
* Open the most recent post on said hashtag.
* Run the bot using 
  >python3 InstagramBot.py 

  and enter the amount of likes you want it to do (anything over 1000 in the span of an hour leads to an account lock, so don't do that...)
* And just wait, the program takes over your mouse during this time so you won't be able to use your computer, 
  it takes a while but only because of the timings emulating a human, 
* PyAutoGui has a failsafe built in if you need to halt the mouse movement, just slam your mouse into the upper-left hand corner while it tries to move the mouse and the script will halt itself

### Setting up Pushbullet phone notifications:
* By default phone notifications using pushbullet are disabled, to enable them go into config.py and change
  >pushbulletnotif = False
  
  to
  >pushbulletnotif = True
  
* Once the notifications are enabled you will need to get your Pushbullet API token, you will need the app on your phone and signed into pushbullet
* You need the Pushbullet API token, you can find this by signing into the desktop website and going to 'My Account' and request a new token
* Put the token in the first line of the file 'pushbullet'
* Now when you run the bot you will get notifications when the bot is finished.
