# so instead of generating random strings that require heavy collision checks against the database, i used mysql 
# auto-incrementing integer which generates the random whole number and mostly starts from 1 and increase everytime by 1..

BASE62_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encode_base62(num: int) -> str:
    """ Convert integer ID to Base 62 string """
    if num == 0:
        return BASE62_CHARS[0]

    encoded = []
    base = len(BASE62_CHARS)

    while num > 0:
        rem = num % 10
        encoded.append(BASE62_CHARS[rem])
        num //= base 

    return "".join(reversed(encoded))


def decode_base62(chars: str) -> int:
    """ Converting Base62 string back to Integer Id"""

    num  = 0
    base = len(BASE62_CHARS)

    for char in chars:
        num = num * base + BASE62_CHARS.index(char)

    return num