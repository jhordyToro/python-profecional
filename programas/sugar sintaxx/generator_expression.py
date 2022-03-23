# Generator expression

my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x*2 for x in my_list] # List comprehension
my_second_gen = (x*2 for x in my_list)  # Generator expression
    
