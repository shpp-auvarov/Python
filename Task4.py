from functools import reduce


class MyNumberClass1:
    """
    The MyNumberClass1 class
    """

    # -----------------------------------------------------
    def __init__(self, number):
        self.number = number

    # print to console text that object is deleted
    def __del__(self):
        print('Object %s was deleted!' % self.number)

    # The function checks that the number is divisible by the divisor without a remainder or not
    def is_divisible_by(self, divisor):
        if divisor == 0:
            return False
        return self.number % divisor == 0

    # Function that multiply two numbers with using Lambda
    @staticmethod
    def multiply_function(x, y):
        return reduce((lambda x, y: x * y), [x, y])


myNumberClass1 = MyNumberClass1(3)
print('myNumberClass1 %s is divisible by %s = %s' % (myNumberClass1.number, 7, myNumberClass1.is_divisible_by(7)))
print('Multiply two numbers %s * %s = %s' % (5, 10, myNumberClass1.multiply_function(5, 10)))


class MyNumberClass2(MyNumberClass1):
    """
    The MyNumberClass2 class
    """

    # -----------------------------------------------------
    _protected_variable = 'protected_value'

    # Check if variable has String type
    def __is_string(self):
        return isinstance(self.number, str)


myNumberClass2 = MyNumberClass2(5)
print("Is myNumberClass2 %s is divisible by %s = %s" % (myNumberClass2.number, 2, myNumberClass2.is_divisible_by(2)))
print('Is myNumberClass2 %s has type of string =' % myNumberClass2.number, myNumberClass2._MyNumberClass2__is_string())
print('Protected variable equal', myNumberClass2._protected_variable)


class MyNumberClass3(MyNumberClass2):
    """
    The MyNumberClass3 class
    """

    # -----------------------------------------------------
    # Function return least common multiple (LCM) and greatest common factor(GCF) of two numbers
    @staticmethod
    def multiply_function(x, y):
        LCM = 0
        for i in range(1, y + 1):
            if x * i % y == 0:
                LCM = x * i
                break
        GCF = (int)((x * y) / LCM)
        return LCM, GCF


myNumberClass3 = MyNumberClass3(10)
LCM, GCF = myNumberClass3.multiply_function(5, 10)
print('Least common multiple of two numbers %s * %s = %s' % (5, 10, LCM))
print('Greatest common factor of two numbers %s * %s = %s' % (5, 10, GCF))
LCM, GCF = myNumberClass3.multiply_function(20, 15)
print('Least common multiple of two numbers %s * %s = %s' % (20, 15, LCM))
print('Greatest common factor of two numbers %s * %s = %s' % (20, 15, GCF))
LCM, GCF = myNumberClass3.multiply_function(14, 21)
print('Least common multiple of two numbers %s * %s = %s' % (14, 21, LCM))
print('Greatest common factor of two numbers %s * %s = %s' % (14, 21, GCF))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x * x, 2), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
