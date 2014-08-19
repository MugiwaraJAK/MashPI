from mashpi import *
import sys
def finish_boil():
	print 'finish boil'
	global Element1
	global Thermo1
	try:
		'''switch off'''
		Element1.setState(True)
		print 'BOILING STEP HAS FINISHED'
		sys.exit(1)
	except KeyboardInterrupt:
		'''switch off'''
		Element1.setState(True)
		print 'BOILING STEP HAS FINISHED'
		sys.exit(1)
	except:
		print 'finish_boil error'
		'''switch off'''
		Element1.setState(True)
		sys.exit(1)
		
