import RPi.GPIO as GPIO

class Element(object):
	state = 0
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	def setState(self,x):
		self.state = x
		GPIO.output(17,x)
	def printState(self):
		if self.state is True:
			print "Current state: off"
		elif self.state is False:
			print  "Current state: on"
		else:
			pass
