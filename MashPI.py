#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
import sys
import glob
import re

# Define thermometer specs
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


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

class Thermo(object):

	def read_temp(self):
		f = open(device_file, 'r')
		lines = f.readlines()
		f.close()
		lines=str(lines)
		match = re.search(r't=?([^\\n>]+)', lines)
		temp_c=match.group(1)
		temp_c = float(temp_c) / 1000.00
		self.temp_c=temp_c
		
def Brew():
	Thermo1=Thermo()
	Element1=Element()
	mash1_timer=0
	mashout_timer=0
	while True:
		Thermo1.read_temp()
		if Thermo1.temp_c>=66:
			'''switch OFF'''
			Element1.setState(True)
			Element1.printState()
		elif Thermo1.temp_c<=66:
			'''switch ON'''
			Element1.setState(False)
			Element1.printState()
			if Thermo1.temp_c>=67:
				'''switch OFF'''
				Element1.setState(True)
				Element1.printState()
			elif Thermo1.temp_c<=66:
				'''switch ON'''
				Element1.setState(False)
				Element1.printState()
		else:
			sys.exit(1)
		time.sleep(60)
		mash1_timer=mash1_timer+1
		if mash1_timer>90:
			while True:
				Thermo1.read_temp()
				if Thermo1.temp_c>=78:
					'''switch OFF'''
					Element1.setState(True)
					Element1.printState()
				elif Thermo1.temp_c<=78:
					'''switch ON'''
					Element1.setState(False)
					Element1.printState()
					if Thermo1.temp_c>=79:
						'''switch OFF'''
						Element1.setState(True)
						Element1.printState()
					elif Thermo1.temp_c<=78:
						'''switch ON'''
						Element1.setState(False)
						Element1.printState()
				else:
					sys.exit(1)
				mashout_timer=mashout_timer+1
				if mash1_timer>15:
					'''switch OFF'''
					Element1.setState(True)
					Element1.printState()
					sys.exit(1)
				elif mash1_timer<15:
					'''switch ON'''
					Element1.setState(False)
					Element1.printState()
				else:
					sys.exit(1)
		elif mash1_timer<90:
			pass
Brew()
