from mashpi import *
import sys

def boil():
	print 'boil'
	global Element1
	global Thermo1
	while True:
		try:
			curr_temp=Thermo1.read_temp()
			if curr_temp < boil_temp:
				'''switch on'''
				if Element1.setState is False:
					'''if already on, pass'''
					pass
				elif Element1.setState is True:
					'''if off then switch on'''
					Element1.setState(False)
					pass
			elif curr_temp>boil_temp:
				'''switch on'''
				Element1.setState(False)
				start_boil=raw_input('Alerady boiling? start boil timer? [y/n]')
				if start_boil=='y' or start_boil=='Y':
					boil_timer = Timer(boil_time, finish_boil)
					boil_timer.start()
				elif start_boil=='n' or start_boil=='N':
					'''switch off'''
					Element1.setState(True)
				else:
					sys.exit(1)
		except KeyboardInterrupt:
			'''switch off'''
			Element1.setState(True)
			print 'BOILING STEP HAS FINISHED'
			sys.exit(1)
		except:
			print 'boil error'
			'''switch off'''
			Element1.setState(True)
			sys.exit()
