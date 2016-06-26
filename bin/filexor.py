"""File Xor Utility

Usage:
    filexor.py <key> <infile> <outfile>
    filexor.py (-h | --help)
    filexor.py (-v | --version)

Options:
    -h --help       Show this screen.
    -v --version    Show version.
"""
from docopt import docopt
from FileXor import fkrandxor


def main(args):
    """Program entry point.

    This takes the arguments and performs the encryption.

    Args:
        args: The dictionary of arguments parsed by docopt

    Returns:
        None

    Raises:
    """
    #todo add file validation through schema
    fkrandxor(args['<key>'], args['<infile>'], args['<outfile>'])

if __name__ == '__main__':
    args = docopt(__doc__, version='File XOR Utility 0.1.0.a1')
    main(args)
