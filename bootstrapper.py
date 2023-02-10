version = 1

print("Contacting EaterMinerXServer...")
print("Please wait, you may need to enable wifi and restart")
print("Connecting...")
import requests, json, sys
url = "https://raw.githubusercontent.com/Eaterminer/animated-palm-tree/main/version"
r = requests.get(url)
print("Preforming version check...")
print(r.text.strip('\n'))
print(version)
if (version == r.text.strip('\n')):
    print("Valid")
else:
    print("Not the Same! your Running an outdated version!")
    print("Please Contact Peter for Assistance.")
    print("Exiting...")
    sys.exit("Reason: Outdated Client! Contact Peter for Assistance")
