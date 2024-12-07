import re

def parse_corrupted_memory(memory):
    mul_pattern = r'mul\((\d+),(\d+)\)'
    
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    total_sum = 0
    mul_enabled = True
    
    mul_matches = re.findall(mul_pattern, memory)
    
    pos = 0
    while pos < len(memory):
        do_match = re.match(do_pattern, memory[pos:])
        if do_match:
            mul_enabled = True
            pos += do_match.end()
            continue
        
        dont_match = re.match(dont_pattern, memory[pos:])
        if dont_match:
            mul_enabled = False
            pos += dont_match.end()
            continue
        
        mul_match = re.match(mul_pattern, memory[pos:])
        if mul_match and mul_enabled:
            x, y = map(int, mul_match.groups())
            total_sum += x * y
            pos += mul_match.end()
            continue
        pos += 1
    
    return total_sum

with open("input6.txt", "r") as file:
    memory = file.read()

print(parse_corrupted_memory(memory))