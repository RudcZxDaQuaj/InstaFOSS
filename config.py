import random
pushbulletnotif = False #Setting this to False will turn off pushbullet notifications, if you 
                        #leave it on True without putting your API token in 'pushbullet' it will cause errors!
#Resolution sets
#mx = random.randrange(504, 524) #720p // also standard laptop resolution
#my = random.randrange(408, 428) #720p // also standard laptop resolution
mx = random.randrange(800, 820) #1080p
my = random.randrange(500, 520) #1080p
ColorDetection = True #Setting this to False won't protect the script from interacting with posts not loaded in yet, instagram might detect that as bot behavior!
ActionBlockDetection = True #Setting this to False won't prevent the script from halting itself at an action block!
