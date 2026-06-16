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

"""
Tên module: students.py

Vai trò:
Lưu trữ dữ liệu sinh viên của hệ thống

Các hàm chính:
Không có

Kiểu import sử dụng:
from data.students import student_records

Tên module: score_utils.py

Vai trò:
Xử lý tính toán điểm trung bình và phân loại học lực.

Các hàm chính:
calculate_average()
classify_student()

Kiểu import sử dụng:
from utils.score_utils import calculate_average
from utils.score_utils import classify_student

Tên module: string_utils.py

Vai trò:
Chuẩn hóa tên sinh viên

Các hàm chính:
normalize_student_names()

Kiểu import sử dụng:
from utils.string_utils import normalize_student_names

Tên module: random_utils.py

Vai trò:
Sinh mã bài tập ngẫu nhiên.

Các hàm chính:
generate_assignment_code()

Kiểu import sử dụng:
import random
import string

Tên module: report_generator.py

Vai trò:
Hiển thị danh sách sinh viên và xuất báo cáo học tập

Các hàm chính:
display_student_scores()
export_learning_report()

Kiểu import sử dụng:
from utils.score_utils import calculate_average
import datetime as dt


Tên module: main.py

Vai trò:
Hiển thị menu và điều hướng các chức năng của chương trình

Các hàm chính:
main()

Kiểu import sử dụng:
from reports.report_generator import display_student_scores


Tên hàm:
calculate_average(scores)

Input:
scores (list)

Output:
float

Module chứa hàm:
score_utils.py

Mô tả luồng xử lý/Pseudocode:
- Kiểm tra danh sách điểm có rỗng hay không
- Khởi tạo tổng điểm và số lượng điểm hợp lệ
- Duyệt từng phần tử trong danh sách điểm
- Nếu phần tử là số thì cộng vào tổng và tăng biến đếm
- Nếu không có điểm hợp lệ thì trả về 0
- Tính và trả về điểm trung bình

Tên hàm:
classify_student(average)

Input:
average (float)

Output:
str

Module chứa hàm:
score_utils.py

Mô tả luồng xử lý/Pseudocode:
- Nếu điểm trung bình lớn hơn hoặc bằng 8 thì trả về "Giỏi"
- Nếu điểm trung bình lớn hơn hoặc bằng 6.5 thì trả về "Khá"
- Nếu điểm trung bình lớn hơn hoặc bằng 5 thì trả về "Trung bình"
- Ngược lại trả về "Yếu"

Tên hàm:
display_student_scores(records)

Input:
records (list)

Output:
Hiển thị thông tin sinh viên ra màn hình

Module chứa hàm:
report_generator.py

Mô tả luồng xử lý/Pseudocode:
- Kiểm tra danh sách sinh viên có rỗng hay không
- Hiển thị tiêu đề danh sách
- Duyệt từng sinh viên
- Tính điểm trung bình bằng hàm calculate_average()
- Phân loại học lực bằng hàm classify_student()
- Hiển thị thông tin sinh viên

Tên hàm:
normalize_student_names(records)

Input:
records (list)

Output:
Danh sách sinh viên đã được chuẩn hóa tên

Module chứa hàm:
string_utils.py

Mô tả luồng xử lý/Pseudocode
- Kiểm tra danh sách sinh viên có rỗng hay không
- Duyệt từng sinh viên
- Xóa khoảng trắng thừa ở đầu và cuối
- Xóa khoảng trắng thừa giữa các từ
- Viết hoa chữ cái đầu mỗi từ
- Cập nhật lại tên sinh viên
- Hiển thị kết quả

Tên hàm:
generate_assignment_code()

Input:
Không có

Output:
str

Module chứa hàm:
random_utils.py

Mô tả luồng xử lý/Pseudocode:
- Tạo tập ký tự gồm chữ cái in hoa và chữ số
- Khởi tạo chuỗi rỗng
- Lặp 4 lần để lấy ngẫu nhiên 4 ký tự
- Ghép các ký tự lại thành mã
- Thêm tiền tố "PY-"
- Trả về mã bài tập

Tên hàm:
export_learning_report(records)

Input:
records (list)

Output:
Tạo file learning_report.txt

Module chứa hàm:
report_generator.py

Mô tả luồng xử lý/Pseudocode:
- Kiểm tra danh sách sinh viên có rỗng hay không
- Tính tổng số sinh viên
- Tính số sinh viên đạt yêu cầu
- Tính số sinh viên cần cải thiện
- Lấy thời gian hiện tại bằng datetime
- Ghi dữ liệu vào file learning_report.txt
- Hiển thị thông báo xuất báo cáo thành công

Tên hàm:
main()

Input:
Không có

Output:
Menu chương trình

Module chứa hàm:
main.py

Mô tả luồng xử lý/Pseudocode:
- Hiển thị menu trong vòng lặp while True
- Nhận lựa chọn từ người dùng
- Nếu chọn 1 thì xem danh sách sinh viên
- Nếu chọn 2 thì chuẩn hóa tên sinh viên
- Nếu chọn 3 thì sinh mã bài tập ngẫu nhiên
- Nếu chọn 4 thì xuất báo cáo học tập
- Nếu chọn 5 thì thoát chương trình
- Nếu nhập sai thì thông báo lỗi
"""