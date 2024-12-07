with open("input3.txt", "r") as file:
    array = [list(map(int, line.split())) for line in file]

numberOfSaveReports = 0

for report in array:
    if all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1)):
        if all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(report[i] > report[i + 1] for i in range(len(report) - 1)):
            numberOfSaveReports += 1

print(numberOfSaveReports)
