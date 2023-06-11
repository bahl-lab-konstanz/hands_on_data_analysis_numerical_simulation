### BASIC DATA TYPES
# In Python we use variables, which are divided into the following primitive data types:
# - boolean, to store binary value True or False

# Boolean variables are the simplest way to implement switches in our scripts, as binary values can also be considered
# as ON and OFF. In fact, we will take advantage of boolean values in the following block. Each line activates a
# different block of code. in the present script.
## Tutorial Navigation
activate_boolean = True
activate_integer = False
activate_float = False
activate_string = False
activate_list = False
activate_dict = False
activate_exercise = False

if activate_boolean:
    print(f"INFO | The data type of variable 'activate_boolean' is {type(activate_boolean)} and its value is {activate_boolean}")

# - integers, to represent positive and negative integer numbers
if activate_integer:
    var_int = 1
    print(f"INFO | The data type of var_int is {type(var_int)} and its value is {var_int}")

# - float, to represent positive and negative floating points numbers
if activate_float:
    var_float = 0.1
    print(f"INFO | The data type of var_float is {type(var_float)} and its value is {var_float}")

# - strings, to store text
if activate_string:
    var_str = "Type here your name"
    print(f"INFO | The data type of var_str is {type(var_str)}. Hello {var_str}!")

# All the data types seen so far are called PRIMITIVE. They are rather simple and powerful, but in many cases we could
# need more complex structures to store our data conveniently. We will have a look at a couple of them now

if activate_list:
    # to initialize lists we use square brackets. We can also initialize empty lists
    var_list_0 = []

    # lists entries can contain objects of any data type
    var_list_1 = [4, "wrong string", None, [], 3.14159]
    print(f"INFO | The data type of var_list_1 is {type(var_list_1)} and its value is {var_list_1}")

    # lists entries can be accessed by indexing from 0 to the length of the list - 1
    # lists are mutable, it means that we can simply change part of our lists by reassigning the elements
    var_list_1[1] = "right string"
    print(f"INFO | We just changed the second element to value '{var_list_1[1]}'")

# There is also the possibility to have data structured in key-value fashion. To this aim we use dictionaris
if activate_dict:
    # to initialize dictionaries we use curly braces. We can also initialize empty dicts
    var_dict_0 = {}

    # dictionaries keys must be of an immutable data type, while values can have any type heterogeneally in a dict
    var_dict_1 = {
        "key_0": 0,
        "key_1": "value",
        "key_2": [2, 2, 2, 2, 2, 2],
        "key_3": {"key_of_the_nested_dict": "value_of_the_nested_dict"}
    }

    # we can easily access values in a dict using keys, referenced using square brackets
    print(f"INFO | our dictionary contains a list: {var_dict_1['key_2']}")


if activate_exercise:
    pass
    # define a list of 10 elements containing floating point numbers going from 1 to 10 and print number 4 out of your
    # variable

