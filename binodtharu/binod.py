#!/bin/python3

import os
import wget
if not (os.path.isfile('gdrive.sh')):
	wget.download('https://raw.githubusercontent.com/GitHub30/gdrive.sh/master/gdrive.sh',bar=bar_thermometer)
	
def binod(fileid):
	print('Binod downloads {} from Google Drive'.format(fileid))
        os.system('curl gdrive.sh | bash -s {}'.format(fileid))

