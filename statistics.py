#Created on CodeAcademy
#Created on 4/9/2016
#Used for personal reference material

#This is a great script to use as a reference for lists with numbers and math. 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade
# the sum()function could be used. this is a manual way of looping through the lists. it can be 
#usefull so never forget how to do it that way
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades)) #Don't forget using float allows the return of a proper value
    return average


# this part is for showing the differene in between the grades
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        square_diff = (average - score) ** 2
        variance += square_diff
    total_variance = variance / len(scores)
    return total_variance
print grades_variance(grades)
        
 #The standard deviation is the square root of the variance. You can 
 #calculate the square root by raising the number to the one-half power
 
 
def grades_std_deviation(variance):
    return variance ** .5

variance = grades_variance(grades)

print grades_std_deviation(variance)
"""        
You've done a great job completing this program. 

We've created quite a few meaningful functions. Namely, we've created helper 
functions to print a list of grades, compute the sum, average, variance, 
and standard deviation about a set of grades.

Let's wrap up by printing out all of the statistics. 

Who needs to pay for grade calculation software when you can write your own? :)
"""

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
