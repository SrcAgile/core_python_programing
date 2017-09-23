#! /usr/bin/env python
'this is the answer of 3.11 about python kernal coding...'
import os
fname = raw_input('enter the name: ')

if os.path.exists(fname):
	fobj = open(fname,'r')
	for ea in fobj:
	    print ea.strip()
	fobj.close()
else:
	print 'the name is not exists...'
