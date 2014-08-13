#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mashpi 2014-08-13
# dovrebbe funzionare tutto!!!!

import RPi.GPIO as GPIO
import time
import os
import sys
import glob
import re
from threading import Timer

# Define thermometer specs
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


# Define recipe properties

mash_temp=65
mash_time=5400 #90 MINUTES
element_cycle=10
thermo_cycle=60
strike_temp=68
boil_temp=97
boil_time=3600


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
		return temp_c

##############
###
###
### brewing steps


def finish_boil():
	try:
		'''switch off'''
		Element1.setState(True)
		print 'BOILING STEP HAS FINISHED'
		sys.exit(1)
	except:
		print 'finish_boil error'
		'''switch off'''
		Element1.setState(True)

def boil():
	try:
		curr_temp=Thermo1.read_temp()
		if curr_temp < boil_temp:
			'''switch on'''
			Element1.setState(False)
			pass
		elif curr_temp>boil_temp:
			start_boil=raw_input('Alerady boiling? start boil timer? [y/n]')
			'''switch on'''
			Element1.setState(False)
			if start_boil=='y' or start_boil=='Y':
				boil_timer = Timer(boil_time, finish_boil)
				boil_timer.start()
			elif start_boil=='n' or start_boil=='N':
				'''switch off'''
				Element1.setState(True)
	except:
		print 'boil error'
		'''switch off'''
		Element1.setState(True)

def finish_mash():
	try:
		remove_the_bag=raw_input('Mash finished, you should remove the bag, type Y when done [y/n]: ')
		if remove_the_bag=='n' or remove_the_bag=='N':
			finish_mash()
		elif remove_the_bag=='y' or remove_the_bag=='Y':
			'''switch off'''
			Element1.setState(True)
		start_boiling_procedure=ra_input('Start boiling procedure? [y/n]: ')
		if start_boiling_procedure=='n' or start_boiling_procedure=='N':
			'''switch off'''
			Element1.setState(True)
		elif start_boiling_procedure=='y' or start_boiling_procedure=='Y':
			boil()
	except:
		print 'boil error'
		'''switch off'''
		Element1.setState(True)

def mashing():
	mash_timer = Timer(mash_time, finish_mash)
	mash_timer.start()
	try:
		curr_temp=Thermo1.read_temp()
		if curr_temp < mash_temp:
			'''switch on'''
			Element1.setState(False)
			sleep(element_cycle)
			'''switch off'''
			Element1.setState(True)
			pass
		elif curr_temp>=mash_temp:
			'''switch off'''
			Element1.setState(True)
			pass
		sleep(thermo_cycle)
	except:
		print 'mash error'
		'''switch off'''
		Element1.setState(True)

def water_heating():
	try:
		curr_temp=Thermo1.read_temp()
		if curr_temp < strike_temp:
			'''switch on'''
			Element1.setState(False)
			pass
		elif curr_temp==strike_temp:
			'''switch off'''
			Element1.setState(True)
			ask_if_add_grain=raw_input('Add grains? [y/n]: ')
			if ask_if_add_grain=='n' or ask_if_add_grain=='N':
				water_heating()
			elif ask_if_add_grain=='y' or ask_if_add_grain=='Y':
				print 'It\'s time to add the grains'
				ask_if_start_mash=raw_input('Start Mash? [y/n]: ')
				if ask_if_start_mash=='n' or ask_if_start_mash=='N':
					water_heating()
				elif ask_if_start_mash=='y' or ask_if_start_mash=='Y':
					mashing()
	except:
		print 'water_heating error'
		'''switch off'''
		Element1.setState(True)

def main():
	water_heating()

main()
