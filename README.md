# InstaFOSS

InstaFOSS is one of my first python projects, it utilizes PyAutoGui and Pushbullet to automatically like posts on Instagram 
with human like reaction times, color recognition for when a post isn't loading properly, image recognition to detect
action blocks and status updates to your phone or other devices using Pushbullets API.

The goal is to mass like specific hashtags so people get notifications leading them to your account, thus gaining more attention,
this works pretty well when doing 500-600 likes in a single run, but pushing it too far could get you an action block.

I've tested this program in my own time and with sparse usage (usually only 2 days a week) over the past couple of months it 
has gotten roughly 400 followers. With daily usage on the right hashtags it could earn maybe 2000 over the course of a month,
of course this isn't the best way to gain followers, but running it in the background on a seperate device does help a lot for smaller 
accounts.

## Getting started:

### Installation:
* Go to the directory you want the bot to be in, it doesn't really matter but it's best to do it either in your home directory *or your user directory if you're using windows so it's easier to navigate to and launch*

  and then
  >git clone https://github.com/RudcZxDaQuaj/InstaFOSS.git

### Requirements:
* Latest version of python 3
* PyAutoGui
* Pushbullet

if you don't wanna install PyAutoGui and Pushbullet manually just go to the InstaFOSS directory and enter
  >pip install -r requirements.txt

this will automatically install all required python libraries.

### Actually running the thing:
* Open a preferred hashtag you want likes or followers from.
* Open the most recent post on said hashtag.
* Change directories to InstaFOSS
  >cd InstaFOSS

* Run the bot using 
  >python3 InstagramBot.py 
  
  or if you're running windows
  >python InstagramBot.py

  and enter the amount of likes you want it to do (anything over 1000 in the span of an hour leads to an account lock, so don't do that...)
* And just wait, the program takes over your mouse during this time so you won't be able to use your computer, 
  it takes a while but only because of the timings emulating a human.
* PyAutoGui has a failsafe built in if you need to halt the mouse movement, just slam your mouse into the upper-left hand corner while it tries to move the mouse     and the script will halt itself

### Config file:
* The config.py file has 3 importent settings,
  >pushbulletnotif #Enables or Disables pushbullet phone notifications
  
  >ColorDetection #Enables or Disables color detection to test if a post has loaded
  
  >ActionBlockDetection #Enables or Disables action block detection
  
* The last two detection settings slow down older devices significantly since they both take and delete screenshots to detect color or insta notifications, so if you are experiencing slow down between posts set those two settings to False

### Setting up Pushbullet phone notifications:
* By default phone notifications using pushbullet are disabled, to enable them go into config.py and change
  >pushbulletnotif = False
  
  to
  >pushbulletnotif = True
  
* Once the notifications are enabled you will need to get your Pushbullet API token, you will need the app on your phone and signed into pushbullet
* You need the Pushbullet API token, you can find this by signing into the desktop website and going to 'My Account' and request a new token
* Put the token in the first line of the file 'pushbullet'
* Now when you run the bot you will get notifications when the bot is finished.

