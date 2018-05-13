dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

dictionary_ms = {
    "name": "Matt",
    "nickname": "babycakes",
    "nationality": "Murican",
    "age": 0
}

print("My name is %s" % (dictionary_ms["name"]))  # My name is Matt
print("Wife calls me %s" %
      (dictionary_ms["nickname"]))  # Wife calls me babycakes
# And by the way I'm Murican
print("And by the way I'm %s" % (dictionary_ms["nationality"]))

dictionary_ms['age'] = 34

# {'nationality': 'Murican', 'age': 34, 'nickname': 'babycakes', 'name': 'Matt'}
print(dictionary_ms)
