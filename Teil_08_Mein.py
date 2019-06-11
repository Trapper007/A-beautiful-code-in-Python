import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

tageswert= defaultdict(list)

with open('Teil_08_Temperatur_Draußen Temp_2.txt') as f:
    for zeile in f:
        datumStr, tempStr = zeile.split('\t')
        datum= (dt.datetime.strptime(datumStr, '%d.%m.%Y %H:%M:%S')).date()
        temp = float(tempStr)

        tageswert[datum].append(temp)

# tagMax = []
# tagMin = []
# tagDatum = []
# die drei zeilen kann man so zusammenfassen
tagMax, tagMin, tagDatum = [], [], []

for key in tageswert:
    maxi = max(tageswert[key])
    mini = min(tageswert[key])
    if abs(maxi) < 40 and abs(mini) < 40:
        tagDatum.append(key)
        tagMax.append(maxi)
        tagMin.append(mini)

fig, ax = plt.subplots()
ax.plot(tagDatum, tagMax, lw=1, label='High',color='red')
ax.plot(tagDatum, tagMin, lw=1, label='Low', color='blue')
ax.fill_between(tagDatum, tagMax, tagMin, facecolor='orange', alpha=0.5)
ax.grid(linestyle='-.', linewidth='0.5', color='green')
ax.legend()
plt.yticks([-10, 0, 25, 30, 35, 40])
plt.show()