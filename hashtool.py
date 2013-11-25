__author__ = 'mcguit1'
import hashlib


class Hashtool():
    def __init__(self):
        pass

    def get_single_hash(self,text,salt,iterations,algorithm):
        salted = (text+salt).encode("utf-8")
        h = hashlib.new(algorithm)
        h.update(salted)
        return h.hexdigest()

    def get_hash(self, text, salt, iterations, algorithm):
        original = (text+salt).encode("utf-8")
        print("---" + salt.encode("utf-8"))
        for x in range(0,iterations):
            h = hashlib.new(algorithm)
            h.update(original + salt)
            original = h.hexdigest()
        return original

