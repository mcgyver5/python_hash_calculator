__author__ = 'mcguit1'
import unittest
from hashtool import Hashtool


class TestHashFunctions(unittest.TestCase):
    def setUp(self):
        self.hashtool = Hashtool()


    def test_md5_hash(self):
        self.assertEqual('d41d8cd98f00b204e9800998ecf8427e',self.hashtool.get_hash('', '', 1, "md5"))
        self.assertEqual('5f4dcc3b5aa765d61d8327deb882cf99',self.hashtool.get_hash('password', '', 1, "md5"))


    #def test_md5_salt(self):
    #    self.assertEqual("b305cadbb3bce54f3aa59c64fec00dea",self.hashtool.get_hash('password','salt',1,"md5"))

    def test_md5_rounds(self):
        self.assertEqual('5f4dcc3b5aa765d61d8327deb882cf99',self.hashtool.get_hash('password', '', 1, "md5"))
        self.assertEqual("696d29e0940a4957748fe3fc9efd22a3",self.hashtool.get_hash('password', '', 2, "md5"))
        self.assertEqual("5a22e6c339c96c9c0513a46e44c39683",self.hashtool.get_hash('password', '', 3, "md5"))

    #def test_md5_salt_rounds(self):
    #    self.assertEqual("25af6b5a72bc966299335d1aabcae3f7",self.hashtool.get_hash('password','salt',2,"md5"))

    #def test_bcrypt(self):
    #    self.assertEqual("the","the")
