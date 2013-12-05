__author__ = 'mcguit1'
import hashlib
import timeit
import bcrypt

class Hashtool():
    def __init__(self):
        pass

    def auth_bcrypt(self,password,hash):
        return True

    def get_bcrypt_hash(self,text,stretchfactor):
        print("again?")
        bcrypt.hashpw(text,bcrypt.gensalt(stretchfactor))
        #move bcrypt stuff here and return timing


    def get_single_hash(self,text,salt,algorithm):
        salted = (text+salt).encode("utf-8")
        h = hashlib.new(algorithm)
        h.update(salted)
        return h.hexdigest()

    def get_hash(self, text, salt, iterations, algorithm):
        if iterations == 1:
            return self.get_single_hash(text,salt,algorithm)
        original = (text+salt).encode("utf-8")
        print("---" + salt.encode("utf-8"))
        for x in range(0,iterations):
            h = hashlib.new(algorithm)
            h.update(original + salt)
            original = h.hexdigest()
        return original

    #input how long you want bcrypt to take and this function returns rounds.
    def tune_bcrypt(self,desired_seconds):
        pass