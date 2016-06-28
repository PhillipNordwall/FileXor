File XOR Stream
===============

Create a file encrypted with a random stream from a key.
--------------------------------------------------------

::


   Usage:
       filexor.py <key> <infile> <outfile>
       filexor.py (-p <padfile>) <infile> <outfile>
       filexor.py (-h | --help)
       filexor.py (-v | --version)
   Options:
       -h --help       Show this screen.
       -p              Use a One-Time-Pad for xor instead of keyed randomness.
       -v --version    Show version.

This file can then be converted back to the original by running this with the
same key again, and the outfile as the input.
