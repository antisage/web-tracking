import time
import hashlib
from datetime import date
from playsound import playsound
from urllib.request import urlopen, Request
import os
from time import gmtime, strftime

def print_time():
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

#Set Directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Target URL to monitor
u = 'https://www.yugioh-card.com/en/products/ms_bewd_platinum.html'

url = Request(u, headers={'User-Agent': 'Mozilla/5.0'})
r_time = 5 #Refresh Time
today = date.today()
response = urlopen(url).read()  
currentHash = hashlib.sha224(response).hexdigest()

print("Starting Monitor Script...")
print("Looking for changes to " + u)
print("Refreshing Every " + str(r_time) + ' seconds')
print_time()

while True:
    try:
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(r_time)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
  
        if newHash == currentHash:
            continue
        else:
            print("CHANGE DETECTED!")
            #Now we gonna beep a number of times
            for i in xrange(15):
                playsound('beep.mp3')
            print_time()
            break
              
    except Exception as e:
        print("Error")