nums = {}
stack = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        for c in line:
            try:
                _ = int(c)
                if len(stack) >= 2:
                    stack.pop()
                stack.append(c)
            except:
                continue
        if len(stack) < 2:
            stack.append(stack[0])
        nums[i] = "".join(stack)
        stack = []
sum = 0
print(nums)
for _, num in nums.items():
    sum += int(num)
print(sum)