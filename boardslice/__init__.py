#!/usr/bin/env python

from pyperclip import copy, paste
from argparse import ArgumentParser
from numpy import array

parser = ArgumentParser(prog='boardslice', description='Slicing and other list operations on the clipboard\'s contents', usage='boardslice [-h] [-e INT] [-j CHAR[S]] [-s CHAR[S]] [a:b] | [i:j, k:l]]')
parser.add_argument('slicer', metavar='[a:b] | [i:j, k:l]', type=str, nargs='*', help='Slice operations for the clipboard\'s contents. For a primer on slice notation, visit https://en.wikipedia.org/wiki/Array_slicing', action='store')
enums = parser.add_mutually_exclusive_group()
enums.add_argument('-e', '--enum', metavar='INT', dest='e', nargs='?', help='Number the lines on output, starting with argument value. Defaults to 1 without argument.', const=1, action='store')
enums.add_argument('-d', '--enumdown', metavar='INT', dest='d', nargs='?', help='Number the lines on output, going down, starting with argument value. Defaults to the number of lines without argument.', const='num', action='store')
parser.add_argument('-s', '--splitdelimiter', metavar='CHAR[S]', dest='s', type=str, help='Character/s to split input on, defaults to \'\\t\'.', default='\t', action='store')
parser.add_argument('-j', '--joindelimiter', metavar='CHAR[S]', dest='j', type=str, help='Character/s to separate output, defaults to \'\\t\'..', default='\t', action='store')
parser.add_argument('-r', '--reverse', dest='r', help='Reverse the order of the lines on output.', action='store_true')
parser.add_argument('-rl', '--reverselines', dest='l', help='Reverse each line on output.', action='store_true')

def main():
	args = parser.parse_args()
	if args.s != None:
		c = array([array(x.split(args.s)) for x in paste().split('\n')])
	else:
		c = array([array(x.split()) for x in paste().split('\n')])
	if args.d == 'num':
		args.d = len(c)
	if args.d != None:
		args.d = int(args.d)
	execarg = 'c=c' + ' '.join(args.slicer)
	try:
		exec(execarg)
	except IndexError:
		print "Your input is not all the same length!"
		print "Check the formatting!"
	lines = [args.j.join(l) for l in c]
	ll = len(lines)
	if args.r:
		lines = lines[::-1]
	if args.l:
		lines = [x[::-1] for x in lines]
	if args.e != None:
		lines = [str(args.e + x) + args.j + lines[x] for x in range(ll)]
	if args.d != None:
		lines = [str(args.d - x) + args.j + lines[x] for x in range(ll)]
	copy('\n'.join(lines))
		
if __name__=="__main__":
	main()
