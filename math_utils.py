def average_grade(roster):
    total = 0
    grade_numbers = 0
    for item in roster:
        total += item.get_grade()
        grade_numbers += 1
    return total/grade_numbers
