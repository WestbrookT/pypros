from collections import deque
import sys


def stack_string(stack):
	out = ""
	for i in stack:
		out += i.lstrip().rstrip() + ' '
	return out


def indent_string(levels):
	out = ""
	for i in levels:
		out += i
	return out

def check_indent(levels, line):
	indent = line[:line.find(line.lstrip())]
	return indent == indent_string(levels)

def build(filename):

	f = open(filename, 'r')

	indent_level = ['']
	selector_stack = deque()
	output = {}
	depth_inc = False

	for line in f:
		if not line.isspace():

			if check_indent(indent_level, line):
				if line.find(';') == -1:
					selector_stack.append(line.rstrip().lstrip())
					output[stack_string(selector_stack)] = []

					depth_inc = True
				else:
					output[stack_string(selector_stack)].append(line)
			else:

				indent = line[:line.find(line.lstrip())]
				if depth_inc and len(indent_string(indent_level)) < len(indent):
					added_indent = indent[len(indent_string(indent_level)):]

					indent_level.append(added_indent)
					output[stack_string(selector_stack)].append(line)
					depth_inc = False
				elif depth_inc:
					selector_stack.pop()
					depth_inc = False
				else:

					while indent_string(indent_level) != indent:

						selector_stack.pop()
						indent_level.pop()
					if line.find(';') == -1:
						selector_stack.append(line.rstrip().lstrip())
						output[stack_string(selector_stack)] = []

						depth_inc = True
					else:
						output[stack_string(selector_stack)].append(line)

	f.close()
	return output

def write(filename, data):

	f = open(filename, 'w')
	out = ''
	for selector in data:
		out += selector + '{\n'
		for i in data[selector]:
			out += '\t' + i.lstrip().rstrip() + '\n'
		out += '}\n\n'

	f.write(out)
	f.close()

def process(filename):
	write(filename+'.css', build(filename+'.pyp'))

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		process(filename)









