#! /usr/bin/env python
# -*- coding:utf-8 -*-
'this is core_python_programing 3.12'
import os
ls = os.linesep
def write():
    while True:
        path = raw_input('enter the file name: ')
	if os.path.exists(path):
	    print 'ERR:%s is already exists' %path
        else:
	    break

    #get the text

    all=[]
    print '\n Enter lines() "." by itself to quit'
    while True:
        text = raw_input('> ')
	if(text=='.'):
	    break
	else:
	    all.append(text)
    with open(path,'w') as f:
	f.writelines(['%s%s' %(x,ls) for x in all])
	f.close()
        print 'WRITE DONE!'
    



def read():
    fname = raw_input('enter the read name: ')
    try:
        fobj = open(fname,'r')
	for eachline in fobj:
	    print eachline.strip()
    except IOError, e:
	print 'open file%s Error' %fname
    else:
	fobj.close()


def show():
    parent = os.getcwd()
    print '======file tree======'
    print '    %s' %parent
    for node in os.listdir('.'):
        print '    |____%s' %node


def delet():
    path = raw_input('enter the dele file: ')
    if os.path.exists(path):
        os.remove(path)
        print 'delete successful!'
    else:
        print 'Error: %s does not exists' %path

if __name__ == '__main__':
    while True:
        print '''please input the target:
		    1)read
		    2)write
                    3)show
                    4)delete
		    5)quit'''
	code = raw_input("which one: ")
	if code=='1':
	    read()
	elif code=='2':
	    write()
        elif code=='3':
            show()
        elif code=='4':
            delet()
	elif code=='5':
            break
	else:
            
	    print 'check your number!'
            print code
