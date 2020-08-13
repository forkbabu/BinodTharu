#!/bin/python3

import os
import wget
if not (os.path.isfile('gdrive.sh')):
	wget.download('https://raw.githubusercontent.com/GitHub30/gdrive.sh/master/gdrive.sh')
	
def binodfunc(fileid):
	os.system('curl gdrive.sh | bash -s {}'.format(fileid))

