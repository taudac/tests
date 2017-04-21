import unittest
import commands
import ftrace

ATT2DB_REG   = 4
ATT2DB_MASK  = 0x0002
ATT2DB_SHIFT = 1

DITHER_REG   = 8
DITHER_MASK  = 0x0003
DITHER_SHIFT = 0

FIRSEL_REG   = 6
FIRSEL_MASK  = 0x0007
FIRSEL_SHIFT = 0

class TestControls(ftrace.TraceReader):

	def __amixer_set(self, control, parameter):
		(status, output) = commands.getstatusoutput(
				'amixer set "{}" "{}"'.format(control, parameter))
		self.assertEqual(status, 0, msg=output)

	def setUp(self):
		self._init_trace()

	def test_att2db(self):
		self.__amixer_set('Anti-Clipping Mode', 'Off')
		self.__amixer_set('Anti-Clipping Mode', 'On')
		self._assert_write('1a', ATT2DB_REG, ATT2DB_MASK, 1 << ATT2DB_SHIFT)
		self._assert_write('1b', ATT2DB_REG, ATT2DB_MASK, 1 << ATT2DB_SHIFT)
		self.__amixer_set('Anti-Clipping Mode', 'Off')
		self._assert_write('1a', ATT2DB_REG, ATT2DB_MASK, 0 << ATT2DB_SHIFT)
		self._assert_write('1b', ATT2DB_REG, ATT2DB_MASK, 0 << ATT2DB_SHIFT)

	def test_dither(self):
		self.__amixer_set('Dither', 'Off')
		self.__amixer_set('Dither', 'RPDF')
		self._assert_write('1a', DITHER_REG, DITHER_MASK, 1 << DITHER_SHIFT)
		self._assert_write('1b', DITHER_REG, DITHER_MASK, 1 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'TPDF')
		self._assert_write('1a', DITHER_REG, DITHER_MASK, 2 << DITHER_SHIFT)
		self._assert_write('1b', DITHER_REG, DITHER_MASK, 2 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'HPDF')
		self._assert_write('1a', DITHER_REG, DITHER_MASK, 3 << DITHER_SHIFT)
		self._assert_write('1b', DITHER_REG, DITHER_MASK, 3 << DITHER_SHIFT)
		self.__amixer_set('Dither', 'Off')
		self._assert_write('1a', DITHER_REG, DITHER_MASK, 0 << DITHER_SHIFT)
		self._assert_write('1b', DITHER_REG, DITHER_MASK, 0 << DITHER_SHIFT)

	def test_filter(self):
		self.__amixer_set('Filter', 'Response 1')
		self.__amixer_set('Filter', 'Response 2')
		self._assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 1 << FIRSEL_SHIFT)
		self._assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 1 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 3')
		self._assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 2 << FIRSEL_SHIFT)
		self._assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 2 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 4')
		self._assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 3 << FIRSEL_SHIFT)
		self._assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 3 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 5')
		self._assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 4 << FIRSEL_SHIFT)
		self._assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 4 << FIRSEL_SHIFT)
		self.__amixer_set('Filter', 'Response 1')
		self._assert_write('1a', FIRSEL_REG, FIRSEL_MASK, 0 << FIRSEL_SHIFT)
		self._assert_write('1b', FIRSEL_REG, FIRSEL_MASK, 0 << FIRSEL_SHIFT)

if __name__ == '__main__':
	# run tests
	unittest.main()

