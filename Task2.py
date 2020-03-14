def task2():
    # creating numerical variable and print to console
    numeric_variable = 1
    print(numeric_variable)

    # creating string variable and print to console
    string_variable = 'Andrey'
    print(string_variable)

    # compare numerical and string variables
    if type(numeric_variable) == type(string_variable):
        print('Have the same type')
    else:
        print('Have the different types')

    # convert numerical variable into string variable
    string_new_variable = str(numeric_variable)
    print("type of new string variable " + string_new_variable + " is: %s" % type(string_new_variable))

    # creating list
    list1 = [1, 2, 3, 4, 5, 6, 6]
    print('list1 = %s' % list1)

    # adding a new element at the end of the list
    list1.append(10)
    print('list1 = %s' % list1)

    # inserting an element in particular index
    insert_at = 3
    list1[insert_at:insert_at] = [20]
    print('list1 = %s' % list1)

    # removing the first element
    list1.pop(0)
    print('list1 = %s' % list1)

    # removing an element via particular index
    index_of_removing = 4
    list1.pop(index_of_removing)
    print('list1 = %s' % list1)

    # reverse of the list
    list1.reverse()
    print('list1 = %s' % list1)

    # size of the list
    print("size of the list1 = %s" % list1.__len__())

    # copy list1 into list2
    list2 = list1.copy()
    print('list2 = %s' % list2)

    # copy list1 into list3
    list3 = list1.copy()
    print('list3 = %s' % list3)

    # sorting list1 with method
    def quick_sorting(list):
        if list.__len__() < 2:
            return list
        else:
            element_of_list = list[0]
            left_list = []
            equal_list = []
            right_list = []
            for checked_element_of_list in list:
                if checked_element_of_list < element_of_list:
                    left_list.append(checked_element_of_list)
                elif checked_element_of_list == element_of_list:
                    equal_list.append(checked_element_of_list)
                elif checked_element_of_list > element_of_list:
                    right_list.append(checked_element_of_list)
        return quick_sorting(left_list) + equal_list + quick_sorting(right_list)

    # sorting with quickSort() function
    list1 = quick_sorting(list1)
    print("quickSort of current list1 = %s" % list1)

    # sorting with sorted() function
    list2 = sorted(list2)
    print('list2 = %s' % list2)

    # sorting with sort() method
    list3.sort()
    print('list3 = %s' % list3)

    # creating list from string "This is a test string for Internship Onix for python" and remove duplicates
    string_variable_2 = 'This is a test string for Internship Onix for python'
    list4 = list(string_variable_2.split(" "))
    print(list4)
    list4 = list(dict.fromkeys(list4))
    print(list4)

    # sort list with reverse order
    list4 = sorted(list4, reverse=True)
    print(list4)

    # creating of dictionary
    dictionary = {'id': '2', 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver',
                  'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'}
    print(dictionary)

    # adding new element to dictionary
    dictionary['full_name'] = 'Janet Weaver'
    print(dictionary)

    # get value via key
    string_variable_3 = dictionary.get('avatar')
    print(string_variable_3)

    # remove element from dictionary
    dictionary.pop('email')
    print(dictionary)

    # get all keys from dictionary
    list_of_keys = dictionary.keys()
    print(list_of_keys)

    # get all values from dictionary
    list_of_values = dictionary.values()
    print(list_of_values)

    # sort dictionary via keys
    dictionaryTemp = {}
    for key in sorted(list_of_keys):
        dictionaryTemp[key] = dictionary.get(key)
    dictionary = dictionaryTemp.copy()
    print(dictionary)

    # sort dictionary via values
    dictionary = sorted(dictionary.items(), key=lambda x: (x[1], x[0]))

    # list to dictionary
    def convert_list_to_dictionary(lst):
        res_dct = {}
        for element in lst:
            res_dct[element[0]] = element[1]
        return res_dct

    dictionary = convert_list_to_dictionary(dictionary)
    print(dictionary)


# Creating the global numerical variable and print to console
numeric_variable = 2
print(numeric_variable)


# Function multiply the numerical variable to the global variable and put the result to list
# Return the list and amount of elements in this list
def multiplication_number_to_global_variable(a):
    global numeric_variable
    list_of_variables = []
    list_of_variables.append(a * numeric_variable)
    return list_of_variables, list_of_variables.__len__()


# Function print the variables from *args and **kwargs to console
def print_to_console_variables(*args, **kwargs):
    print(args)
    print(kwargs)


# The function checks that the number is divisible by the divisor without a remainder or not
def is_divisible_by(num, divisor):
    return num % divisor == 0


# The function that calculates the Fibonacci number
def fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    before_the_last_number = 0
    last_number = 1
    for i in range(2, n + 1):
        number = before_the_last_number + last_number
        before_the_last_number = last_number
        last_number = number
    return number


if __name__ == "__main__":
    task2()
    print(multiplication_number_to_global_variable(2))
    print("Result of executing function of print_to_console_variables: ")
    print_to_console_variables([1, 2, 3], a=2, b='Andrey')
    print(is_divisible_by(10, 3))
    print(is_divisible_by(10, 5))
    for i in range(0, 20):
        print(fibonacci_number(i))
