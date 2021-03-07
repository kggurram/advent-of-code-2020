
f = open('D:\Projects\GitHub\Advent of Code 2020\Day 1 - Report Repair\inputs.txt', 'r')
nums = []
entries = []
ans = 0;

for line in f.readlines():
    nums.append(int(line))

nums.sort()

def two_ents():
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == 2020:
            entries.append(nums[l])
            entries.append(nums[r])
            return entries
        elif nums[l] + nums[r] < 2020:
            l += 1
        else:
            r -= 1
    return 0

def three_ents():
    for i in range(0, len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            if nums[i] + nums[l] + nums[r] == 2020:
                
                entries.append(nums[i])
                entries.append(nums[l])
                entries.append(nums[r])
                return entries
            elif nums[i] + nums[l] + nums[r] < 2020:
                l += 1
            else:
                r -= 1
    return 0

#two_ents()
#ans = entries[0] * entries[1]

#three_ents()
#ans = entries[0] * entries[1] * entries[2]

#print(ans)