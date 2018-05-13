
dictionary = {"some_key": "some_value"}

for key in dictionary:
    print("%s --> %s" % (key, dictionary[key]))

# some_key --> some_value

for key, value in dictionary.items():
    print("%s --> %s" % (key, value))

# some_key --> some_value

dictionary_ms = {
    "name": "Matt",
    "nickname": "babycakes",
    "nationality": "Murican",
    "age": 34
}

for attribute, value in dictionary_ms.items():
    print("My %s is %s" % (attribute, value))

# My name is Matt
# My nickname is babycakes
# My nationality is Murican
# My age is 34
