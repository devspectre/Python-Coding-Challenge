import sys
import re

sample_input = "11:22:33:44:55:66 aaa\na6:ae:2f:9d:31:b4\nbbb\n"

pattern = '([a-f0-9]{2}[:]{1}){5}([a-f0-9]{2}){1}'

def find_first_valid_mac_addr(string: str) -> str:
	result = []
	lines = string.split('\n')
	for line in lines:
		match = re.compile(pattern).finditer(line)
		if match:
			for y in match:
				found = line[y.start():y.end()]
				if y.start() == 0 and y.end() == len(line):
					return line

	return ''

sys.stdout.write(find_first_valid_mac_addr(sample_input))