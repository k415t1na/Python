import re
from unittest import TestCase
import unittest

class Book:
	name_pattern = re.compile(r'^[A-Za-z0-9 .]+$') #Allow only letters, digits, spaces and dot

	def __init__(self, name, publishing_year):
		
		self.__name = name if self.name_pattern.search(name) else 'no name'

		self.__publishing_year = publishing_year if publishing_year > 0 else 'no year'

		if self.__name == 'no name':
			print(f'Name: {name} was invalid!')

		if publishing_year < 1:
			print(f'Year: {publishing_year} is not positive!')


	def get_name(self):
		return self.__name


	def set_name(self, new_name):
		self.__name = new_name if self.name_pattern.search(new_name) else 'no name'

		if self.__name == 'no name':
			print(f'Name: {new_name} was invalid!')


	def get_publishing_year(self):
		return self.__publishing_year

	def set_publishing_year(self, new_publishing_year):
		self.__publishing_year = new_publishing_year if new_publishing_year > 0 else 'no year'
		if new_publishing_year < 1:
					print(f'Year: {new_publishing_year} is not positive!')


	def get_type(self):
		return 'book'


class ChristmasBook(Book):
	
	# Since duplicates won't be allowed, 
	# we will be using set for authors

	__authors = set()

	def __init__(self, name, publishing_year, authors):
		super().__init__(name, publishing_year)
		self.__authors.update(authors)


	def get_number_of_authors(self):
		return len(self.__authors)


	def add_authors(self, new_authors):
		self.__authors.update(new_authors)


	def get_type(self):
		pre = 'christmas'
		return f'{pre}{super().get_type()}'


	
def task_1():
	book1 = Book('Kristina Myftaraga JR. 3rd', 2000 )
	print(book1.get_name()) # Kristina Myftaraga JR.
	print(book1.get_publishing_year()) # 2000
	print(book1.get_type())
	print()
	book2 = Book('Kristina @Myftaraga', -2201)
	print(book2.get_name()) # no name
	print(book2.get_publishing_year()) # no year
	print(book2.get_type())


def task_2():
	christmas_book = ChristmasBook('Christmas Book', 2012, [])
	print(christmas_book.get_number_of_authors()) # 0
	christmas_book.add_authors(['Third','Fourth', 'First', 'First'])
	print(christmas_book.get_number_of_authors()) # 3
	print(christmas_book.get_type()) # 3


def task_3(filename):

	book_dictionary = {
		'christmasbook': [],
		'book': []
	}
	with open(f'./{filename}.csv', 'r') as books_file:

		for line in books_file:

			# rstrp() to ignore the newline char
			book_info = line.rstrip().split(';')
			
			book_name = book_info[0]
			book_authors = book_info[1].split('|')
			book_publish_year = int(book_info[2])
	
			if book_name.find('Christmas') != -1:
				ch_book_object = ChristmasBook(book_name, book_publish_year, book_authors)
				book_dictionary['christmasbook'].append(book_name)
			else:
				ch_book_object = Book(book_name, book_publish_year)
				book_dictionary['book'].append(book_name)


	print('\n Stats \n')
	print('christmasbook: ', len(book_dictionary['christmasbook'])) 
	print('book: ', len(book_dictionary['book'])) 
	print('\n --- \n')



class TestBook(TestCase):
	
	def setUp(self):
		self.book1 = Book('Kristina Myftaraga JR. 3rd', 2000 ) # correct
		self.book2 = Book('Kristina @Myftaraga', -2201) # incorrect

	def test_name_correct(self):
		''' Test when name is done correctly '''

		self.assertEqual('Kristina Myftaraga JR. 3rd', self.book1.get_name())
		self.assertEqual(2000, self.book1.get_publishing_year())

	
	def test_set_name(self):

		book_object = Book('Bad Name@', 2012)
		self.assertEqual(book_object.get_name(), 'no name')
		book_object.set_name('Good Name')
		self.assertEqual(book_object.get_name(), 'Good Name')
	

	def test_set_year(self):

		book_object = Book('Bad Name', -2012)
		self.assertEqual(book_object.get_publishing_year(), 'no year')

		book_object.set_publishing_year(2012)
		self.assertEqual(book_object.get_publishing_year(), 2012)
	
	


def main():
	# task_3('input')
	unittest.main()


if __name__ == "__main__":
   main()

   