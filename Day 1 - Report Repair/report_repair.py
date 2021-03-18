f = open('D:\Projects\GitHub\Advent of Code 2020\Day 1 - Report Repair\inputs.txt', 'r') # open given input file
nums = [] # array initialized for numbers in input file
entries1 = [] # entries array for Part 1
entries2 = [] # entries array for Part 2
ans1 = 0; # initialized answer for Part 1
ans2 = 0; # initialized answer for Part 2

# for each line in the inputs file
for line in f.readlines(): 
    nums.append(int(line)) # add each number as an element to nums[]

nums.sort() # sort the numbers

# Part 1
def two_ents():
    # l and r used as substitutes for left and right rulers
    l = 0
    r = len(nums) - 1
    while l < r: # while the left ruler has not reached the right
        # if the 2 numbers add up to 2020, add the 2 numbers to entries1[]
        if nums[l] + nums[r] == 2020: 
            entries1.append(nums[l])
            entries1.append(nums[r])
            return entries1
        # if the 2 numbers add up to be less than 2020, keep going lol 
        elif nums[l] + nums[r] < 2020:
            l += 1
        else:
            r -= 1
    return 0

# Part 2
def three_ents():
    # l and r used as substitutes for left and right rulers
    for i in range(0, len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r): # while the left ruler has not reached the right
            # if the 3 numbers add up to 2020, add the 3 numbers to entries2[]
            if nums[i] + nums[l] + nums[r] == 2020:
                entries2.append(nums[i])
                entries2.append(nums[l])
                entries2.append(nums[r])
                return entries2
            # if the 3 numbers add up to be less than 2020, keep going lol
            elif nums[i] + nums[l] + nums[r] < 2020:
                l += 1
            else:
                r -= 1
    return 0

# Part 1 Solution
two_ents() # run Part 1 function
ans1 = entries1[0] * entries1[1] # product of the 2 elements of entries1[] 
print(ans1) # print answer

# Part 2 Solution
three_ents() # run Part 2 function
ans2 = entries2[0] * entries2[1] * entries2[2] # product of the 2 elements of entries2[]
print(ans2) # print answer