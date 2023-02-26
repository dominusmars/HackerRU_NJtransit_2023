from motortest import Motor
import time
 
motors = Motor()

def distance_traveled(time_elapsed):
	circumference = .1885
	rps = 200/60
	mps = circumference * rps
	return time_elapsed * mps

#input row size in meters
def move_row(row_size):
	start = time.time()
	motors.motorupA()
	motors.motorupB()
	while distance_traveled(time.time()-start)< row_size:
		time.sleep(1)
	motors.motorstopA()
	motors.motorstopB()

def move_row_back(row_size):
	start = time.time()
	motors.motordownA()
	motors.motordownB()
	while distance_traveled(time.time()-start)< row_size:
		time.sleep(1)
	motors.motorstopA()
	motors.motorstopB()
	
move_row_back(1)
