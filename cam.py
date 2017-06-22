def to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
word=input("Enter a string: ")
print(to_camel(word))
