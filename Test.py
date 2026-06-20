from tabulate import tabulate

class Employee:
    def __init__(self, id, name, salary_day, work_days, allowance):
        self.id = id
        self.name = name
        self.salary_day = salary_day
        self.work_days = work_days
        self.allowance = allowance

    def calculate_income(self):
        return (self.work_days * self.salary_day) + self.allowance
        
    def classify_income(self):
        total_income = self.calculate_income()
        if total_income < 9000000:
            return "Thấp"
        elif total_income < 15000000:
            return "Trung Bình"
        elif total_income < 30000000:
            return "Khá"
        else:  
            return "Cao"

class EmployeeManager:
    def __init__(self):
        self.employees = [Employee("123", "Kien", 500, 24, 100)]
    
    def add_employee(self):
        id = input("Mã NV: ").strip()
        if not id:
            print("Mã NV không rỗng")
            return
            
        for emp in self.employees:
            if emp.id.upper() == id.upper():
                print("Không trùng mã NV")
                return
                
        name = input("Họ tên: ").strip()
        if not name:
            print("Họ tên không rỗng")
            return

        try:
            salary_day = float(input("Lương ngày: "))
            if salary_day < 0:
                print("Lương ngày ≥ 0")
                return
                
            work_days = float(input('Số ngày công: '))
            if not (0 <= work_days <= 31):
                print("Ngày công: 0 → 31")
                return
                
            allowance = float(input("Phụ cấp: "))
            if allowance < 0 :
                print("Phụ cấp ≥ 0")
                return
        except ValueError:
            print("Lỗi: Vui lòng nhập định dạng số hợp lệ!")
            return
            
        new_employee = Employee(id, name, salary_day, work_days, allowance)
        self.employees.append(new_employee)
        print("Đã thêm nhân viên thành công!")

    def show_all(self):
        employees_data = []
        for emp in self.employees:
            employees_data.append([
                emp.id, 
                emp.name, 
                emp.salary_day, 
                emp.work_days, 
                f"{emp.allowance:,.0f}", 
                f"{emp.calculate_income():,.0f}", 
                emp.classify_income()
            ])
        table = tabulate(employees_data, headers=["Mã NV", "Họ tên", "Lương ngày", "Số ngày công", "Phụ cấp", "Tổng thu nhập", "Loại thu nhập"], tablefmt="grid")
        print(table)

    def update_employee(self):
        id = input("Mã NV: ").strip()
        if not id:
            print("Mã NV không rỗng")
            return
            
        target_employee = None
        for emp in self.employees:
            if emp.id.upper() == id.upper():
                target_employee = emp
                break
                
        if not target_employee:
            print("Nhân viên không tồn tại!")
            return

        try:
            salary_day = float(input("Lương ngày: "))
            if salary_day < 0:
                print("Lương ngày ≥ 0")
                return
                
            work_days = float(input('Số ngày công: '))
            if not (0 <= work_days <= 31):
                print("Ngày công: 0 → 31")
                return
                
            allowance = float(input("Phụ cấp: "))
            if allowance < 0 :
                print("Phụ cấp ≥ 0")
                return
        except ValueError:
            print("Lỗi: Vui lòng nhập định dạng số hợp lệ!")
            return
            
        target_employee.salary_day = salary_day
        target_employee.work_days = work_days
        target_employee.allowance = allowance
        print("Thông báo cập nhật thành công")

    def delete_employee(self):
        id = input("Mã NV: ").strip()
        if not id:
            print("Mã NV không rỗng")
            return
            
        for emp in self.employees:
            if emp.id.upper() == id.upper():
                choice = input("Bạn có chắc muốn xóa nhân viên này không? (Y/N): ")
                if choice.upper() == "Y":
                    self.employees.remove(emp)
                    print(f"Bạn đã xóa thành công nhân viên ID: {id}")
                elif choice.upper() == "N":
                    pass
                else:
                    print("Vui lòng chọn Y hoặc N!")
                return
                
        print("Nhân viên không tồn tại!")

    def search_employee(self):
        id = input("Mã NV: ").strip()
        if not id:
            print("Mã NV không rỗng")
            return
            
        for emp in self.employees:
            if emp.id.upper() == id.upper():
                employees_data = [[
                    emp.id, emp.name, emp.salary_day, emp.work_days, 
                    f"{emp.allowance:,.0f}", f"{emp.calculate_income():,.0f}", emp.classify_income()
                ]]
                table = tabulate(employees_data, headers=["Mã NV", "Họ tên", "Lương ngày", "Số ngày công", "Phụ cấp", "Tổng thu nhập", "Loại thu nhập"], tablefmt="grid")
                print(table)
                return
                
        print("Không tìm thấy nhân viên phù hợp")

def main():
    manager = EmployeeManager()
    while True:
        choice = input("""================ MENU ================
1. Hiển thị danh sách nhân viên
2. Thêm nhân viên mới
3. Cập nhật nhân viên
4. Xóa nhân viên
5. Tìm kiếm nhân viên
6. Thoát
=====================================
Nhập lựa chọn của bạn: """)
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_employee()
            case "3":
                manager.update_employee()
            case "4":
                manager.delete_employee()
            case "5":
                manager.search_employee()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý nhân sự!")
                break
            case _:
                print("Vui lòng chọn lựa chọn từ [1-6]!")

if __name__ == "__main__":
    main()
