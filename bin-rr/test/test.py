import struct
def bit_string(irr, num_bloombits):
  """Like bin(), but uses leading zeroes, and no '0b'."""
  s = ''
  bits = []
  for bit_num in xrange(num_bloombits):
    if irr & (1 << bit_num):
      bits.append('1')
    else:
      bits.append('0')
  return ''.join(reversed(bits))


bloom = 0
bloom_bits = [3]
bloom |= (1 << 3)
print bloom
print bit_string(bloom, 10)


def to_big_endian(i):
  return struct.pack('>L', i)

print to_big_endian(1010)