# BinaryStream

BinaryStream library for python

## What is it?

This is a library for convenient serialization of standard C/C++ types similar to that used for example in RakNet
protocol.

## Installation

**For Linux/Mac**

```commandline
pip3 install binary-stream
```

**For Windows**

```commandline
pip install binary-stream
```

## Usage

**Example**

```python
from binary_stream import BinaryStream

write_stream = BinaryStream()

write_stream.write_int8(42)
write_stream.write_bool(True)
write_stream.write_bool(True)

data = write_stream.get_buffer()
print(data.hex())

read_stream = BinaryStream(data)

print(read_stream.read_int8())
print(read_stream.read_bool())
print(read_stream.read_bool())
```

## Credits

This project is inspired by [binary_utils](https://github.com/Podrum/binary_utils)

## License

This project is open sourced under MIT license, see the [LICENSE](LICENSE) file for more details.