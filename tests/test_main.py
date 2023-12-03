import unittest
from binary_stream import BinaryStream


class MainTest(unittest.TestCase):
    def setUp(self):
        self.read_buffer = []

    def _write_signed(self):
        self.binary_stream.write_int8(42)
        self.binary_stream.write_int16(42)
        self.binary_stream.write_int24(42)
        self.binary_stream.write_int32(42)
        self.binary_stream.write_int64(42)

    def _write_unsigned(self):
        self.binary_stream.write_uint8(42)
        self.binary_stream.write_uint16(42)
        self.binary_stream.write_uint24(42)
        self.binary_stream.write_uint32(42)
        self.binary_stream.write_uint64(42)

    def _write_float(self):
        self.binary_stream.write_float16(42.2)
        self.binary_stream.write_float32(42.2)
        self.binary_stream.write_float64(42.2)

    def _write_bool(self):
        self.binary_stream.write_bool(True)
        self.binary_stream.write_bool(False)

    def _all_write(self):
        self._write_signed()
        self._write_unsigned()
        self._write_float()
        self._write_bool()

    def _read_signed(self):
        self.read_buffer.append(self.binary_stream.read_int8())
        self.read_buffer.append(self.binary_stream.read_int16())
        self.read_buffer.append(self.binary_stream.read_int24())
        self.read_buffer.append(self.binary_stream.read_int32())
        self.read_buffer.append(self.binary_stream.read_int64())

    def _read_unsigned(self):
        self.read_buffer.append(self.binary_stream.read_uint8())
        self.read_buffer.append(self.binary_stream.read_uint16())
        self.read_buffer.append(self.binary_stream.read_uint24())
        self.read_buffer.append(self.binary_stream.read_uint32())
        self.read_buffer.append(self.binary_stream.read_uint64())

    def _read_float(self):
        self.read_buffer.append(self.binary_stream.read_float16())
        self.read_buffer.append(self.binary_stream.read_float32())
        self.read_buffer.append(self.binary_stream.read_float64())

    def _read_bool(self):
        self.read_buffer.append(self.binary_stream.read_bool())
        self.read_buffer.append(self.binary_stream.read_bool())

    def _read_all(self):
        self._read_signed()
        self._read_unsigned()
        self._read_float()
        self._read_bool()

    def test_write(self):
        self.binary_stream = BinaryStream()
        self._all_write()
        buffer = self.binary_stream.get_buffer()
        data = buffer.hex()
        self.assertEqual(data, '2a002a00002a0000002a'
                               '000000000000002a2a00'
                               '2a00002a0000002a0000'
                               '00000000002a51464228'
                               'cccd404519999999999a0100')

    def test_read(self):
        data = '2a002a00002a0000002a000000000000002a2a002a00002a0000002a000000000000002a51464228cccd404519999999999a0100'
        self.binary_stream = BinaryStream(bytes.fromhex(data))
        self._read_all()
        data = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42.1875, 42.20000076293945, 42.2, True, False]
        self.assertListEqual(self.read_buffer, data)
