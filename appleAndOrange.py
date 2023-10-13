# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. *A negative value of d means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. *
# Apple and orange(2).png

# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

# For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range  so we print

# 1
# 2
# Function Description

# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# Input Format

# The first line contains two space-separated integers denoting the respective values of  and .
# The second line contains two space-separated integers denoting the respective values of  and .
# The third line contains two space-separated integers denoting the respective values of  and .
# The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
# The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .

def countApplesAndOranges(startH, endHouse, locApple, locOrange, apples, oranges):
    # Write your code here

    apps = 0
    ors = 0
    for apple in apples:

        distanceApp = locApple + apple

        if distanceApp in range(startH, endHouse + 1):
            apps += 1
    for orange in oranges:
        distancOr = locOrange + orange
        if distancOr in range(startH, endHouse + 1):
            ors += 1

    print(apps)
    print(ors)
