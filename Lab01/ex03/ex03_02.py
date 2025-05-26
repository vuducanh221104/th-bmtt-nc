def dao_nguoc_list(lst):
  """
  Đảo ngược thứ tự các phần tử trong một danh sách.

  Args:
    lst: Danh sách cần đảo ngược.

  Returns:
    Một danh sách mới với các phần tử theo thứ tự ngược lại.
  """
  return lst[::-1]

# Nhập danh sách số từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)