import re
import os
import glob
# Define thermometer specs
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
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
