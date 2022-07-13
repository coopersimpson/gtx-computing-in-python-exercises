#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.
#
#Hint: one common issue on this problem is that every line
#in the input file ends with a line break except the last
#one. If the autograder gives you an index error, open
#top500result.txt and make sure there are 500 lines in your
#output file!


#Write your function here!

def sort_films(filename, destination_file):
    input_file = open(filename, "r")
    sort_nums = []

    for line in input_file:
        line1 = line.split("\t")
        line2 = line1[1].strip("\n")
        sort_nums.append(line2)
        sort_nums.sort(reverse=True)
    
    i = 0
    for i in range(len(sort_nums)):
        output_file = open(destination_file, "a")
        for line in open(filename):
            line1 = line.split("\t")
            line2 = line1[1].strip("\n")
            if sort_nums[i] == line2:
                print(line1[0] + "\t", line2, file = output_file)
                i += 1
                break
            else:
                pass

    input_file.close()
    output_file.close()


#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")





