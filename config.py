import random
pushbulletnotif = False #Setting this to True will turn on pushbullet notifications, if you 
                        #leave it on True without putting your API token in 'pushbullet' will cause errors!

#Resolution sets: un-comment which ever resolution your monitor running instagram has and comment out the ones that don't.
#mx = random.randrange(504, 524) #720p // also standard laptop resolution
#my = random.randrange(408, 428) #720p // also standard laptop resolution
mx = random.randrange(800, 820) #1080p
my = random.randrange(500, 520) #1080p

ColorDetection = True #Setting this to False won't protect the script from interacting with posts 
                      #not loaded in yet, instagram might detect that as bot behavior!

ActionBlockDetection = True #Setting this to False won't prevent the script from halting itself at an action block!
                            #But if you're experiencing lag in between posts try disabling this to see if it helps.

MoreStatusInfo = True #Setting this to True will give more information on progress and percentages.
