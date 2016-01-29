a = """
morning get ready process 25 5
drive 50 7
park 8 4
walk to room 7 4
prep time 12 8
"""

activities = []
for l in a.split('\n'):
  l = l.strip()
  if len(l) < 3: continue
  d, stdD = [float(x) for x in l.split(' ')[-2:]]
  # print d, stdD
  rev = l[::-1]
  s2 = rev.find(' ', rev.find(' ')+1)
  a = l[:-s2].strip()
  # print a
  activities.append((a, d, stdD))
# activities = [
#                ('get ready', 25, 5),
#                ('drive', 50, 7),
#                ('park', 8, 4),
#                ('walk to room', 7, 4),
#                ('prep time', 12, 8),
#              ]

from datetime import datetime, timedelta

def make_time(t):
  # hour, minute
  return datetime(1990,1,1,t[0],t[1],0)

def add_times(t1, delta):
  # delta is in minutes
  return t1 + timedelta(0,60*delta)

endTime = make_time((11,30))

activities.reverse()

longestKeyLen = max([len(x[0]) for x in activities])

averageTime = worstTime = mediocreTime = endTime

ret = []
for a, avD, wStdDD in activities:
  wD = avD + wStdDD
  mD = avD + (float(wStdDD) / 2)
  averageTime = add_times(averageTime, -avD)
  worstTime = add_times(worstTime, -wD)
  mediocreTime = add_times(mediocreTime, -mD)

  s = 'START: ' + a + '   ' + (' ' * (longestKeyLen - len(a))) + mediocreTime.strftime('%H:%M')
  # s = 'START: ' + a + '   ' + (' ' * (longestKeyLen - len(a))) + worstTime.strftime('%H:%M') + ' to ' + averageTime.strftime('%H:%M')
  ret.append(s)

ret.reverse()
print '\n'.join(ret)


