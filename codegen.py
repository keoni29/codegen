# TODO use comment blocks or similar to doxygen
import argparse

_parser = argparse.ArgumentParser(description='Generate source code using inline python code in the source.')
_parser.add_argument('filename')
_parser.add_argument('-x', action='store_true', help='Enables code execution.')

_args = _parser.parse_args()

with open(_args.filename, 'rb') as _f:
	_executable_code = ''
	for _line_no, _line in enumerate(_f):
		if '$' in _line:
			_idx = _line.index('$')
			_executable_code += _line[_idx + 1:]
		else:
			if len(_executable_code):
				if _args.x:
					exec(_executable_code)
				else:
					print 'exec('
					print _executable_code,
					print '\t)'
			_executable_code = ''

			if _args.x:
				print _line.rstrip()