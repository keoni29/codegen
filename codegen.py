"""
	codegen

	Execute code in comment blocks of target source code file to generate code.
"""
import argparse

""" All variable names are prefixed with _ so the target can use 
	whatever variable names it wants """

class _col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

_parser = argparse.ArgumentParser(description='Generate source code using inline python code in the source.')
_parser.add_argument('filename')
_parser.add_argument('-x', action='store_true', help='Enable code execution')
_parser.add_argument('-l',type=str, choices=['vhdl','c'], default='vhdl', help='Language for comment style.')

_args = _parser.parse_args()

# Define markers here
_marker = {
	'vhdl':['--<',['--'],'-->'],
	'c':['/*<',['//','*'],'*/']
}

_start_marker = _marker[_args.l][0]
_block_marker = _marker[_args.l][1]
_end_marker = _marker[_args.l][2]

_code_block = False
_block_count = 0

with open(_args.filename, 'rb') as _f:
	_executable_code = ''

	for _line_no, _line in enumerate(_f):

		if _code_block:
			if _end_marker in _line:
				# Execute code when end of block is detected.
				if len(_executable_code):
					if _args.x:
						exec(_executable_code)
					else:
						print _col.BOLD + 'exec('
						print _executable_code,
						print '\t)' + _col.ENDC
				_executable_code = ''
				_code_block = False
				_block_count += 1
			else:
				for _marker in _block_marker:
					if _marker in _line:
						if _line.lstrip().index(_marker) == 0:
							# Inline python code is commented.
							_line = _line.lstrip()[len(_marker):]
							break

				# Remove comment marker from executable string.
				_executable_code += _line
					
		else:
			if _start_marker in _line:
				_code_block = True
			else:
				print _line.rstrip()
		
if _code_block:
	print _col.WARNING + '[WARNING] Missing end marker!' + _col.ENDC
if _block_count == 0:
	print _col.WARNING + '[WARNING] No executable code found!' + _col.ENDC

if not _args.x:
	print _col.WARNING + '[WARNING] Executing inline code can be potentially dangerous. Please review the code before executing it using the -x option.' + _col.ENDC