# import another_module
#
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# # Module -> Class -> Object
# # Under object: attributes & methods
#
# timmy = Turtle()  # turtle module -> Turtle class -> create Turtle class object called timmy
# print(timmy)  # <turtle.Turtle object at 0x000001FBB0C00890> printed a turtle objected saved at a location memory
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)  # print the height which is the ATTRIBUTE of the object my_screen
# my_screen.exitonclick()  # This is a METHOD -> Exit the program when click
#
# # Documentation here: https://docs.python.org/3/library/turtle.html

from prettytable import PrettyTable #from prettytable package import PrettyTable Class
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
# Could be useful for quant signal display, texting and email

# Access the attribute instead of using method. Change align attribute to 'l'
table.align = 'l'
print(table.align)
print(table)
