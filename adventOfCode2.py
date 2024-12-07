from collections import Counter

with open("input2.txt", "r") as file:
    data = file.readlines()

left_list = []
right_list = []

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

right_counts = Counter(right_list)

similarity_score = sum(left * right_counts[left] for left in left_list)

print("Similarity score:", similarity_score)