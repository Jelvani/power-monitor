
import matplotlib.pyplot as plt
import argparse

time = []
power= []


parser = argparse.ArgumentParser(
                prog='plot.py',
                description='Plot logfiles from `monitor.py`')
parser.add_argument('logfile',help='Path to a logfile') 
args = parser.parse_args()

with open(args.logfile,"r") as f:
    lines = [line.rstrip() for line in f]
    for l in lines:
        s = l.split()
        time.append(float(s[0]))
        power.append(float(s[1]))

plt.style.use('ggplot')
plt.xlabel("Time")
plt.ylabel("Watts")
plt.plot(time,power)
plt.show()
