class WarehouseDecorator:
    """Packaging decorator for different items."""
    def __init__(self, material):
        self.material = material

        # The __call__ method enables to write classes
        # where the instances behave like functions and
        # can be called like a function.
    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('Wrapping items from {} with {}'.
                  format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


# when we call the decorator with args, the function is passed to the __call__
# method, instead we pass the args to the  __init__ method
@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

# outputs...
# Wrapping items from pack_books with kraft
# We'll pack books: ('Alice in Wonderland', 'Winnie the Pooh')
#
# Wrapping items from pack_toys with foil
# We'll pack toys: ('doll', 'car')
#
# Wrapping items from pack_fruits with cardboard
# We'll pack fruits: ('plum', 'pear')

# Explanation...
# To make your object callable, the Class need to defined it as one with the
# __call__ special method.
