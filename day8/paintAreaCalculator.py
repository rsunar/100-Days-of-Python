#Write your code below this line ๐
# number of cans = (wall height โ๏ธ wall width) รท coverage per can.
import math
def paint_calc(test_h,test_w,coverage):
    no_of_can =(test_h*test_w)/coverage
    print(f"You'll need {math.ceil(no_of_can)} cans of paint.")







#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   
no_of_can = 0
# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(test_h,test_w,coverage)