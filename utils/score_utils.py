def calculate_average(scores):
    if len(scores) == 0:
        return 0

    total = 0
    count = 0

    for score in scores:
        if (type(score) == int or type(score) == float):
            total += score
            count += 1

    if count == 0:
        return 0

    return total / count


def classify_student(average):
    if (average >= 8):
        return "Giỏi"
    elif (average >= 6.5):
        return "Khá"
    elif (average >= 5):
        return "Trung bình"
    else:
        return "Yếu"
