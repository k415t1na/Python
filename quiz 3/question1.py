#Define an abstract class named Store, which has two non-public data items – name and income.
#Add an initializer with default values for each data items and getters/setters for the data items.
#Override the less than operator (__lt__) to check whether the income of the right operand is less than the left operant income.
#Add an abstract method display.

#Create a class called CarStore, which inherits the Store class.
#Add a non-public data member to store the number of employees in the CarStore class and getter/setter.
#Add an initializer to initialize the three (own and base) data members.
#Override the abstract method display to display on the screen the number of employees in the store. Override the __str__ to return the information about the CarStore class.


from abc import ABC, abstractmethod


class Store(ABC):

	def __init__(self, name="Store", income=100):
		self.__name = name
		self.__income = income

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def getIncome(self):
		return self.__income

	def setIncome(self, income):
		self.__income=income

	def __lt__(self, other_store):
		# Override the less operator check if right is lower than left
		return self.__income > other_store.__income

	@abstractmethod
	def display(self):
		raise NotImplementedError("NotImplementedError")



class CarStore(Store):


	def __init__(self, name, income, num_of_employees):
		super(CarStore, self).__init__(name, income)
		self.__num_of_employees = num_of_employees

	def getNumEmployees(self):
		return self.__num_of_employees

	def setNumEmployees(self, num_of_employees):
		self.__num_of_employees = num_of_employees

	def display(self):
		# Show number of employees
		to_display = f'Number of employees: {self.__num_of_employees}'
		print(to_display)


	def __str__(self):
		# Info about the CarStore Class
		to_return = f'Info about Store:\n Name: {super(CarStore, self).getName()} \n Income: {super(CarStore, self).getIncome()}  '
		return to_return




def main():
	car_store_obj1 = CarStore('Benz', 12000, 23)
	car_store_obj2 = CarStore('Volvo', 14000, 13)

	print(car_store_obj1)




if __name__ == "__main__":
	main()