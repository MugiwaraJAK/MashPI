from mashpi import *
import sys
def finish_mash():
	print 'finish mash'
	global Element1
	global Thermo1
	while True:
		try:
			remove_the_bag=raw_input('Mash finished, you should remove the bag, type Y when done [y/n]: ')
			if remove_the_bag=='n' or remove_the_bag=='N':
				pass
			elif remove_the_bag=='y' or remove_the_bag=='Y':
				'''switch off'''
				Element1.setState(True)
				start_boiling_procedure=raw_input('Start boiling procedure? [y/n]: ')
				if start_boiling_procedure=='n' or start_boiling_procedure=='N':
					'''switch off'''
					Element1.setState(True)
					pass
				elif start_boiling_procedure=='y' or start_boiling_procedure=='Y':
					boil()
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
