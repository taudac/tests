import unittest
import commands
import os
import re

tracing_path = '/sys/kernel/debug/tracing/'
enable_i2c_events_cmd = 'echo 1 > events/i2c/enable'
clear_trace_cmd = 'echo "" > trace'

ATT2DB_REG   = 4
ATT2DB_MASK  = 0x0002
ATT2DB_SHIFT = 1

DITHER_REG   = 8
DITHER_MASK  = 0x0003
DITHER_SHIFT = 0

FIRSEL_REG   = 6
FIRSEL_MASK  = 0x0007
FIRSEL_SHIFT = 0

class TestControls(unittest.TestCase):

	def __amixer_set(self, control, parameter):
		(status, output) = commands.getstatusoutput(
				'amixer set "{}" "{}"'.format(control, parameter))
		self.assertEqual(status, 0, msg=output)

	def __assert_write(self, address, reg, mask, val):
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

	def setUp(self):
		os.chdir(tracing_path)
		os.system(enable_i2c_events_cmd)
		os.system(clear_trace_cmd)

	def test_att2db(self):
		self.__amixer_set('Anti-Clipping Mode', 'Off')
		self.__amixer_set('Anti-Clipping Mode', 'On')
		self.__assert_write('1a', ATT2DB_REG, ATT2DB_MASK, 1 << ATT2DB_SHIFT)
		self.__assert_write('1b', ATT2DB_REG, ATT2DB_MASK, 1 << ATT2DB_SHIFT)
		self.__amixer_set('Anti-Clipping Mode', 'Off')
		self.__assert_write('1a', ATT2DB_REG, ATT2DB_MASK, 0 << ATT2DB_SHIFT)
		self.__assert_write('1b', ATT2DB_REG, ATT2DB_MASK, 0 << ATT2DB_SHIFT)

	def test_dither(self):
		self.__amixer_set('Dither', 'Off')
		self.__amixer_set('Dither', 'RPDF')
		self.__assert_write('1a', DITHER_REG, DITHER_MASK, 1 << DITHER_SHIFT)
		self.__assert_write('1b', DITHER_REG, DITHER_MASK, 1 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'TPDF')
		self.__assert_write('1a', DITHER_REG, DITHER_MASK, 2 << DITHER_SHIFT)
		self.__assert_write('1b', DITHER_REG, DITHER_MASK, 2 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'HPDF')
		self.__assert_write('1a', DITHER_REG, DITHER_MASK, 3 << DITHER_SHIFT)
		self.__assert_write('1b', DITHER_REG, DITHER_MASK, 3 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'Off')
		self.__assert_write('1a', DITHER_REG, DITHER_MASK, 0 << DITHER_SHIFT)
		self.__assert_write('1b', DITHER_REG, DITHER_MASK, 0 << DITHER_SHIFT)

	def test_filter(self):
		self.__amixer_set('Filter', 'Response 1')
		self.__amixer_set('Filter', 'Response 2')
		self.__assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 1 << FIRSEL_SHIFT)
		self.__assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 1 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 3')
		self.__assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 2 << FIRSEL_SHIFT)
		self.__assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 2 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 4')
		self.__assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 3 << FIRSEL_SHIFT)
		self.__assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 3 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 5')
		self.__assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 4 << FIRSEL_SHIFT)
		self.__assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 4 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 1')
		self.__assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 0 << FIRSEL_SHIFT)
		self.__assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 0 << FIRSEL_SHIFT)

if __name__ == '__main__':
	# run tests
	unittest.main()

