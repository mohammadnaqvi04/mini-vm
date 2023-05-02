import struct, sys
from ast import literal_eval

if __name__ == '__main__':
    try:
        bytelist = literal_eval(sys.argv[1])
        result = [struct.pack("<B", b) for b in bytelist]
        for b in result:
            sys.stdout.write(b)
    except IndexError:
        print "USAGE: python bc.py [BYTE_VALUE_LIST]"
        print "\nExample:\n\tpython bc.py '[0,2,43,0,  3,2,0,0,  0,1,1,0,  0,0,0,0]'"
