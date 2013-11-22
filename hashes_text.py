import sys


def get_hash(text)

salt = ""
algorithm = "MD5"
iterations = 1

if len(sys.argv) < 2:
  print("Usage: hashes_text.py [sometext] [algorithm] [# of iterations] [salt]")
  print ("defaults are empty string md5,1,null")
  print ("so, here is the md5 hash of empty string")
  print get_hash("")
  
for arg in sys.argv:
  print(arg)
