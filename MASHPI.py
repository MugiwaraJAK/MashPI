#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mashpi 2014-08-18

__author__ = 'cristian@mariolini.net'
__version__ = '0.6a'

import RPi.GPIO as GPIO
import time
import os
import sys
import glob
import re
from threading import Timer
from thermo import *
from element import *
from water_heating import *
from mashing import *
from finish_mash import *
from boil import *
from finish_boil import *


# Define recipe properties

mash_temp=30
mash_time=15 #90 MINUTES
element_cycle=10
thermo_cycle=5
strike_temp=29
boil_temp=33
boil_time=10

#define thermo sensor and heating element
Element1=Element()
Thermo1=Thermo()

##########################
# Main function
def main():
	try:
		print 'main'
		water_heating()
		global Element1
		global Thermo1
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()
