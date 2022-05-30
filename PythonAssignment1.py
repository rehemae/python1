# Write a function that accepts any number of integers as positional arguments and any number of a student's
#  attributes as keyword arguments and prints the result of multiplying all of the integers with a customized
#   greeting based on the keyword arguments. Name the function multiply_and_greet.


from itertools import product


def multiply_and_greet(*args, **kwargs):
    product=1
    for a in args:
        product*=a
    print (product)
    keys=kwargs.keys()
    if "country" in keys:
        print (f"Hello {kwargs['name']} from {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs["age"]
        print (f"Hello {kwargs['name']} your born in {year}")

    elif "name"  in keys:
        print (f"Hello {kwargs['name']}")
    else:
        print (f"Hello Anonymous")





    