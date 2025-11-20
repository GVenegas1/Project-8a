
#project-8a

#Gabriel Venegas
#GitHub username: GVenegas1
#Date: 11/19/2025
#Description:
"""This function takes a list of numbers and changes each number into its square.
The original list is updated directly"""

def square_list(numbers):

    # Go through each number in the list along with its index
    for i in range(len(numbers)):

        #Replace the numbers with its squared
        numbers[i] = numbers[i] ** 2

#Example
#nums= [7,-3,12,9]
#square_list(nums)
#print(nums)