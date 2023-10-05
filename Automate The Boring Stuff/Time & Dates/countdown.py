import time, subprocess

timeLeft = 60
while timeLeft > 0:
  print(timeLeft, end = "")
  time.sleep(1)
  timeLeft = timeLeft - 1

# at the end 
subprocess.Popen(["Start", 'alarm.wav'], shell = True)