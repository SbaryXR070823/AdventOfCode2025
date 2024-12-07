import re

with open("input5.txt", "r") as file:
    memory = file.read()

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
matches = re.findall(pattern, memory)

total_sum = sum(int(x) * int(y) for x, y in matches)

print(total_sum)
