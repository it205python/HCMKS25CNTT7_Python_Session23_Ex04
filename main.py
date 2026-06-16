from data.students import student_records
from reports.report_generator import (display_student_scores, export_learning_report)
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code


def main():
    while True:

        print("""
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================
""")

        choice = input("Chọn chức năng (1-5): ")

        match choice:
            case "1":
                display_student_scores(student_records)
            case "2":
                normalize_student_names(student_records)
            case "3":
                print("--- SINH MÃ BÀI TẬP ---")
                print("Mã bài tập của bạn là:", generate_assignment_code())
            case "4":
                export_learning_report(student_records)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()