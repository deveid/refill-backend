import hashlib
import hmac
import struct
import base64
import random

def dt(mac):
    hdig = mac.hexdigest()
    offset = int(hdig[-1], 16)
    p = hdig[offset * 2 : offset * 2 + 8]
    return int(p, 16) & 0x7fffffff

def hotp(c=349012, n=6):
    """Generate an HOTP token.
    ``k``
        Key; bytestring of length 20.
    ``c``
        Counter; integer in range 0 .. 2**64 - 1
    ``n``
        Token length; integer in {6,7,8}
    """
    r=random.randrange(0,2000)
    k=bytearray(r)
    mac = hmac.new(k, struct.pack(">Q", c), hashlib.sha1)
    s = dt(mac)
    return "{:06}".format(s % 10 ** n)
