with open("input3.txt", "r") as file:
    array = [list(map(int, line.split())) for line in file]

def is_safe(report):
    if all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1)):
        if all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(report[i] > report[i + 1] for i in range(len(report) - 1)):
            return True
    return False

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

numberOfSaveReports = 0

for report in array:
    if is_safe(report) or is_safe_with_dampener(report):
        numberOfSaveReports += 1

print(numberOfSaveReports)
