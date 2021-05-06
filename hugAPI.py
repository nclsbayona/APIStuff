import hug
from random import randint, choice, shuffle
from json import dumps

"""Simple API to test, some of the HUG capabilities"""

lib = dict()

@hug.get(['/all','/'])
def get_all():
    """Returns all available objects"""
    return eval(dumps(lib, indent=4))

@hug.get('/only_one')
def get_this(this: hug.types.number):
    """Returns an specific object"""
    return eval(dumps(lib[this], indent=4))

@hug.get('/new')
def get_new_this():
    """Includes a new object"""
    key=len(lib)+1
    value=list(choice(str("BNnb1001191743"+"$%&/#@=?*, ")) for i in range(randint(16,32)))
    shuffle(value)
    value=''.join(value)
    lib[key]=value
    return {
        key:value
    }

@hug.put('/new_one')
def put_new(obj: hug.types.Chain(hug.types.number, hug.types.text)):
    """Usage of post"""
    print(obj)