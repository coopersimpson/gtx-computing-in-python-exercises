#In the previous problem, you were given a dictionary where
#the keys were names and the values were days of activity
#on a class forum. You returned the name of the most active
#student; or, more simply, the key corresponding to the
#highest value.
#
#In this problem, you'll do the same thing, but with a more
#complex data structure. Your function should be called
#most_active, and it should have one parameter.
#
#Instead of a dictionary, your parameter is a list of
#dictionaries. Every dictionary in the list will have exactly
#two keys: 'name' and 'days_active'. Your goal, as before,
#is to return the name of the most active student.
#
#Some of the code you wrote on the previous problem will be
#reusable, but you'll need to modify it.
#
#Hint: you do NOT need to iterate over the keys in the
#dictionaries inside the lists. You can always just access
#the_dict["name"] and the_dict["days_active"] directly.
#Your only loop should be the loop over the list.


#Add your code here!

def most_active(the_list):
    # in the lambda (anon) function the x is essentially replaced with:
    # {"name": "Joyner, David", "days_active": 14}["days_active"]
    # that statement evaluates to 14
    # that would be the first iterable, and the same is applied to
    # each dictionary in the list, then the max is returned
    output = max(the_list, key=lambda x: x["days_active"])
    return output["name"]
    
    # also works
    # return max(the_list, key=lambda x: x["days_active"])["name"]
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Chopra, Deepak
the_list = [{"name": "Joyner, David", "days_active": 14},
            {"name": "Chopra, Deepak", "days_active": 22},
            {"name": "Winfrey, Oprah", "days_active": 17}]
print(most_active(the_list))
