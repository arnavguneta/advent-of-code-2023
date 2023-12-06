nums = {}
stack = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.replace("one","one1one").replace("two","two2two").replace("three","three3three").replace("four","four4four").replace("five","five5five").replace("six","six6six").replace("seven","seven7seven").replace("eight","eight8eight").replace("nine","nine9nine")
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