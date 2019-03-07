
import subprocess
import getpass
import time
import sys

app = sys.argv[1]

# to only list processes of the current user
user = getpass.getuser()
get = lambda x: subprocess.check_output(x).decode("utf-8")
# get the initial window list
ws1 = get(["wmctrl", "-lp"]); t = 0
# run the command to open the application
subprocess.Popen(app)

while t < 30:
    # fetch the updated window list, to see if the application's window appears
    ws2 = [(w.split()[2], w.split()[0]) for w in get(["wmctrl", "-lp"]).splitlines() if not w in ws1]
    # see if possible new windows belong to our application
    procs = sum([[(w[1], p) for p in get(["ps", "-u", user]).splitlines() \
              if app[:15].lower() in p.lower() and w[0] in p] for w in ws2], [])
    # in case of matches, move/resize the window
    if len(procs) > 0:
        subprocess.call(["xdotool", "windowsize", "-sync", procs[0][0] , "100%", "100%"])
        break
    time.sleep(0.5)
    t = t+1