import unittest
import os
import re

tracing_path = '/sys/kernel/debug/tracing/'
enable_i2c_events_cmd = 'echo 1 > events/i2c/enable'
clear_trace_cmd = 'echo "" > trace'

class TraceReader(unittest.TestCase):

	def _assert_write(self, address, reg, mask, val):
		with open('trace', 'r') as trace:
			t = trace.readlines()
			if address == '1a':
				i = -4
			elif address == '1b':
				i = -2
			else:
				assertTrue(false, msg='Invalid reg {}'.fotmat(address))
			p = re.compile(r'(i2c_write)|(a=0{})|l=\d.*\[(.*)\]'.format(address))
			m = p.findall(t[i])
			self.assertEqual(3, len(m), msg='Failed parsing trace!')
			d = m[2][2].split('-')
			# check reg
			self.assertEqual(reg, int(d[0], 16)>>1)
			# check val
			dval = (((int(d[0], 16) << 8) & 0x01) | int(d[1], 16)) & mask
			self.assertEqual(val, dval)

	def _init_trace(self):
		os.chdir(tracing_path)
		os.system(enable_i2c_events_cmd)
		os.system(clear_trace_cmd)

