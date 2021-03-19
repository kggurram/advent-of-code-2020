f = open('D:\Projects\GitHub\Advent of Code 2020\Day 2 - Password Philosophy\inputs.txt', 'r') # open given input file
inputs = [] # initialized array for given inputs
nums = [] # initialized array for the given numbers (subsection from inputs)
letters = [] # initialized array for the result of modifiying init_letters[]
pw = [] # initialized array for the given passwords (subsection from inputs)
valid_pw = [] # final array for valid password elements
init_letters = [] # initialized array for first iteration of letter array (to be used to create the neater, better letters[])
test = []

# for each line in inputs file, split into inputs[]
for line in f.readlines():
    inputs.append(line.split())

# sort sections into arrays 
def sort_into_arr():
    # for each input, sort subsections into respective arrays
    for i in range(len(inputs)):
        nums.append(inputs[i][0].split("-")) # move number sections to num[] while ignoring the "-"
        init_letters.append(inputs[i][1].split(":")) # move letters into init_letters[] while ignoring the ":"
        pw.append(inputs[i][2]) # move passwords into pw[]

sort_into_arr() # run the array sorting function
# for each element in init_letters
for i in range(len(init_letters)):
    init_letters[i].remove('')
    letters.append(init_letters[i][0]) # update letters[] with each modified element such that letters is a polished array, unlike init_letters; a messy array

# checks for valid passwords
def valid():
    # for each password
    for i in range(len(pw)):
        # if the given letter is in the relating password
        if(letters[i] in pw[i]):
            # if the position of the letter in the password matches with either of the 2 given numbers for that password
            if(((pw[i].index(letters[i]) + 1) == nums[i][0]) or ((pw[i].index(letters[i]) + 1) == nums[i][1])):
                valid_pw.append(pw[i]) # add that password to valid_pw[]

valid() # run to check for valid password and update valid_pw[]
print(len(valid_pw)) # print length of valid_pw denoting the number of valid passwords
print(valid_pw)