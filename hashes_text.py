import sys
import hashlib
import argparse
from hashtool import Hashtool


def allowed_alg(algstring):
    if algstring.lower() in hashlib.algorithms:
        return algstring
    else:
        msg = "algorithm not recognized"
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser(description="hash incoming text")
parser.add_argument('--text','-t', default='')
parser.add_argument('--alg','-alg',default='md5',type=allowed_alg)
parser.add_argument('--iterations','-it',default=1,type=int)
parser.add_argument('-salt',default='')
args = parser.parse_args()
h = Hashtool()
print(args.alg + " hash of " + args.text + " is " +h.get_hash(args.text,args.salt,args.iterations,args.alg))
