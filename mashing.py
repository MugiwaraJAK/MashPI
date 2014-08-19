from mashpi import *
import sys
def mashing():
	print 'mashing'
	global Element1
	global Thermo1
	mash_timer = Timer(mash_time, finish_mash)
	mash_timer.start()
	while True:
		try:
			curr_temp=Thermo1.read_temp()
			if curr_temp < mash_temp:
				print curr_temp
				'''switch on'''
				Element1.setState(False)
				time.sleep(element_cycle)
				'''switch off'''
				Element1.setState(True)
				pass
			elif curr_temp>=mash_temp:
				print curr_temp
				'''switch off'''
				Element1.setState(True)
				pass
			else:
				sys.exit(1)
			time.sleep(thermo_cycle)
		except KeyboardInterrupt:
			'''switch off'''
			Element1.setState(True)
			print 'BOILING STEP HAS FINISHED'
			sys.exit(1)
		except:
			print 'mash error'
			'''switch off'''
			Element1.setState(True)
