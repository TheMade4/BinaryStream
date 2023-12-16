import struct


class BinaryStream:
    def __init__(self, data: bytes = bytes(), pos: int = 0):
        self.buffer = data
        self.pos = pos

    def seek(self, pos):
        self.pos = pos

    def write(self, data):
        self.buffer += data

    def read(self, length=-1):
        if length < 0:
            length = len(self.buffer) - self.pos
        data = self.buffer[self.pos:self.pos + length]
        self.pos += length
        return data

    def get_buffer(self):
        return self.buffer

    def read_int8(self):
        return struct.unpack("!b", self.read(1))[0]

    def read_uint8(self):
        return struct.unpack("!B", self.read(1))[0]

    def read_int16(self):
        return struct.unpack("!h", self.read(2))[0]

    def read_uint16(self):
        return struct.unpack("!H", self.read(2))[0]

    def read_int24(self):
        data = self.read(3)
        return struct.unpack("!i", (b"\x00" if data[2] < 0x80 else b"\xff") + data)[0]

    def read_uint24(self):
        return struct.unpack("!I", b"\x00" + self.read(3))[0]

    def read_int32(self):
        return struct.unpack("!i", self.read(4))[0]

    def read_uint32(self):
        return struct.unpack("!I", self.read(4))[0]

    def read_int64(self):
        return struct.unpack("!q", self.read(8))[0]

    def read_uint64(self):
        return struct.unpack("!Q", self.read(8))[0]

    def read_float16(self):
        return struct.unpack("!e", self.read(2))[0]

    def read_float32(self):
        return struct.unpack("!f", self.read(4))[0]

    def read_float64(self):
        return struct.unpack("!d", self.read(8))[0]

    def read_bool(self):
        return struct.unpack("!?", self.read(1))[0]

    def write_int8(self, value):
        self.write(struct.pack("!b", value))

    def write_uint8(self, value):
        self.write(struct.pack("!B", value))

    def write_int16(self, value):
        self.write(struct.pack("!h", value))

    def write_uint16(self, value):
        self.write(struct.pack("!H", value))

    def write_int24(self, value):
        self.write(struct.pack("!i", value)[1:])

    def write_uint24(self, value):
        self.write(struct.pack("!I", value)[1:])

    def write_int32(self, value):
        self.write(struct.pack("!i", value))

    def write_uint32(self, value):
        self.write(struct.pack("!I", value))

    def write_int64(self, value):
        self.write(struct.pack("!q", value))

    def write_uint64(self, value):
        self.write(struct.pack("!Q", value))

    def write_float16(self, value):
        self.write(struct.pack("!e", value))

    def write_float32(self, value):
        self.write(struct.pack("!f", value))

    def write_float64(self, value):
        self.write(struct.pack("!d", value))

    def write_bool(self, value):
        self.write(struct.pack("!?", value))
