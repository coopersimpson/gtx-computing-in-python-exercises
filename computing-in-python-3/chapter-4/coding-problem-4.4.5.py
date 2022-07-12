#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!

def find_net_force(forces):
    total_horizontal = 0
    total_vertical = 0
    
    for force in forces:
        magnitude, angle = force
        angle = radians(angle)
        horizontal = magnitude * cos(angle)       
        vertical = magnitude * sin(angle)
        total_horizontal += horizontal
        total_vertical += vertical

    net_magnitude = sqrt(total_horizontal**2 + total_vertical**2)
    net_magnitude = round(net_magnitude, 1)
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)
    return (net_magnitude, net_angle)

# forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
# print(find_net_force(forces))


# Function to convert file to a list of tuples
def find_net_force_from_file(filename):
    input_file = open(filename, "r")
    output_list = []
    for line in input_file:
        line = [int(n) for n in line.split()]
        line_tuple = tuple(line)
        output_list.append(line_tuple)
    input_file.close()
    # List of tuples as argument to existing function
    return find_net_force(output_list)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))