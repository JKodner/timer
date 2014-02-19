import time, sys, pygame
time_count = 0
second = " "
count_minute = " "
count_hour = " "
def sep(s, n):
	print s * n
sep(" ", 1)
sep("#", 50)
print """Welcome to the Python Tiner!
All You Need To Do is to Input a Second, Minute, and Hour"
And the Computer Will Do The Rest!"""
print """
Type CTL-C to Pause the Timer and Type it Twice to Exit."""
sep("#", 50)
sep(" ", 1)
sep("-*-", 1)
while type(second) != int and type(count_minute) != int and type(count_hour) != int:
	try:
	    second = int(raw_input("Seconds:"))
	    count_minute = int(raw_input("Minutes:"))
	    count_hour = int(raw_input("Hours:"))
	    if second > -1 and count_minute > -1 and count_hour > -1: 
	        if second > 59:
	            second = " "
	            count_minute = " "
	            count_hour = " "
	            print "The Second Measurement Must Be Less Than 60."
	    else:
	        second = " "
	        count_minute = " "
	        count_hour = " "
	        print "Each Time Measurement Must Be Greater Than or Equal to 0."
	except ValueError: None
time_count += second
time_count += count_minute * 60
time_count += count_hour * 3600
def start_end():
	global second
	global count_minute
	global count_hour
	now = time.localtime()
	print "Timer Set For: %s:%s:%s" % (str(count_hour).zfill(2), str(count_minute).zfill(2), str(second).zfill(2))
	print "Timer Set At Time: %s:%s:%s" % (str(now.tm_hour).zfill(2), str(now.tm_min).zfill(2), str(now.tm_sec).zfill(2))
	end_hour = now.tm_hour + count_hour
	end_minute = now.tm_min + count_minute
	end_second = now.tm_sec + second
	print "Timer Will End At: %s:%s:%s" % (str(end_hour).zfill(2), str(end_minute).zfill(2), str(end_second).zfill(2))
sep("-*-", 1)
sep(" ", 1)
raw_input("Type Anything to Set The Timer.")
sep(" ", 1)
for i in range(time_count):
	try:
	    time.sleep(1)
	except KeyboardInterrupt:
	    try:
	        sep(" ", 1)
	        sep(" ", 1)
	        sep("-", 50)
	        raw_input("Timer Paused: Type Anything to Continue The Timer.")
	        sep("-", 50)
	        sep(" ", 1)
	    except KeyboardInterrupt:
	        print " "
	        sep("-", 50)
	        print " "
	        print "Exiting the Program..."
	        print " "
	        sys.exit()
time.sleep(1)
pygame.init()
pygame.mixer.Sound('/Users/jacobkodner/Downloads/beep-6.wav').play()
time.sleep(0.2)
print """
Timer Finished.
"""