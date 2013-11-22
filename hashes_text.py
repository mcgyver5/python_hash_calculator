import sys
import hashlib
import argparse

def get_hash(text,salt,iterations,algorithm):
    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def get_md5_hash(text):

    m = hashlib.md5()
    m.update(text.encode("utf-8"))
    return m.hexdigest()



def allowed_alg(algstring):
    if algstring.upper() in hashlib.algorithms_available:
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
my_it_args = vars(parser.parse_args())

print(args.alg + " hash of " + args.text + " is " +get_hash(args.text,args.salt,args.iterations,args.alg))
