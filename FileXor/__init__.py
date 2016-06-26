import hashlib
import random
import codecs
import operator


def krandgen(key):
    """Provide a keyed byte generator

    Args:
        key: A string that will be used as the key for the genereator.

    Returns:
        A 8-bit randomness generator.

    Raises:
    """
    khash = hashlib.sha256(codecs.encode(key, 'utf-8')).digest()
    random.seed(khash)
    while True:
        yield random.getrandbits(8)

def fkrandxor(key, infile, outfile):
    """Encrypt an input file to an output file using a random xor stream
    obtained from the key as a seed

    Args:
        key: The key used to seed the random xor stream
        infile: The file to xor
        outfile: The file to write the xored output to.

    Returns:
        Nothing, there is a side effect of writing to outfile

    Raises:
    """
    gen = krandgen(key)
    with open(infile, "rb") as fin:
        with open(outfile, 'wb') as fout:
            fout.write(bytes(map(operator.xor, fin.read(), gen)))
