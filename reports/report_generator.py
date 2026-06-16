from utils.score_utils import (calculate_average, classify_student)
import datetime as dt
from colorama import Fore


def display_student_scores(records):
    if (not records):
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start=1):
        average = calculate_average(student["scores"])
        level = classify_student(average)

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - "
            f"{level}"
        )
    print("---------------------------------")


def export_learning_report(records):
    if (not records):
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed_students = 0
    failed_students = 0

    for student in records:
        average = calculate_average(student["scores"])

        if (average >= 5):
            passed_students += 1
        else:
            failed_students += 1

    report_time = dt.datetime.now()


    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write("BÁO CÁO HỌC TẬP")
        file.write(f"Thời gian tạo: {str(report_time)} \n")
        file.write(f"Tổng số sinh viên: {str(total_students)} \n")
        file.write(f"Số sinh viên đạt yêu cầu: {str(passed_students)} \n")
        file.write(f"Số sinh viên cần cải thiện: {str(failed_students)} \n")

    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students} \n")
    print(f"Số sinh viên đạt yêu cầu: {passed_students} \n")
    print(f"Số sinh viên cần cải thiện: {failed_students} \n")
    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt")
