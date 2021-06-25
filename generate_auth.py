import hashlib 
import time

def getNewAuth():
  # your PRIVATE API KEY
  api_key = "YOUR_PRIVATE_API_KEY"

  # get timestamp e.g. 1624605441.85469
  ts = time.time() #returns the unix timestamp e.g. 1624605441.85469

  # remove the decimal from ts e.g. 1624605441~~.85469~~
  ts = int(ts) # 1624605441

  # get the 7bits from ts e.g. 1624605~~441~~
  ts = str(t)[:-2] # e.g. 1624605
  
  # concatenate the ts(timestamp) and apikey
  to_be_encrypted = ts + api_key # e.g. 1624605YOUR_PRIVATE_API_KEY

  # encrypt it to md5
  auth_check = hashlib.md5(tobeMD5.encode())
  # get the auth value
  newAuth = auth_check.hexdigest() # e.g. 3062a08e62a42d5cac708efd2c918d41
  
  return newAuth

old_auth = getNewAuth()
minutesStart = 1;
while True:
    time.sleep(60);
    print("old: ", oldAuth)
    newAuth = getNewAuth()
    print("new: ", newAuth)
    if oldAuth == newAuth:
        print("Still equal")
        print("How many minutes?: ",str(minutesStart));
        minutesStart += 1
    else:
        print("Not equal anymore");
        print("How many minutes?: ",str(minutesStart));
        minutesStart += 1
