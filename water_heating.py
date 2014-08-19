from mashpi import *
import sys
def water_heating():
	print 'heating'
	global Element1
	global Thermo1
	while True:
		try:
			curr_temp=Thermo1.read_temp()
			if curr_temp < strike_temp:
				'''switch on'''
				Element1.setState(False)
				print curr_temp
				time.sleep(thermo_cycle)
				pass
			elif curr_temp>=strike_temp:
				print curr_temp
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
					else:
						sys.exit()
				else:
					pass
			else:
				sys.exit(1)
		except KeyboardInterrupt:
			'''switch off'''
			Element1.setState(True)
			print 'BOILING STEP HAS FINISHED'
			sys.exit(1)
		except:
			print 'water_heating error'
			'''switch off'''
			Element1.setState(True)
