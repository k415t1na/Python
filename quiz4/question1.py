import unittest


def magic(list_elements, target):
    if target in list_elements:
        return "yes"
    if target % 2:
        return "magic"
    return "no"


class TestMagic(unittest.TestCase):

	def test_yes(self):
		''' Target in list lements '''
		self.assertEqual(magic([1,3], 1), "yes")

	def test_no(self):
		''' Target not in list lements and even '''
		self.assertEqual(magic([1,3], 2), "no")

	def test_magic(self):
		''' Test number is odd '''
		self.assertEqual(magic([1,3], 5), "magic")



def main():

	unittest.main()






		

if __name__ == "__main__":
	main()
