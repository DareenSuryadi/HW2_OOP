from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password = password

    def login(self, email, password):
        if email == self._email and password == self._password:
            return True
        else:
            return False

    @abstractmethod
    def logout(self):
        pass

    def get_user_id(self):
        return self._user_id

class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.enrollment_id = enrollment_id
        self.courses = []
        self.grades = []
        self.absences = []

    def enroll_in_course(self, course):
        self.courses.append(course)

    def record_absence(self, date):
        self.absences.append(date)

    def logout(self):
        pass

class Professor(User):
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.faculty_id = faculty_id
        self.courses_taught = []
        self.academic_calendar = None

    def upload_grades(self, student_id, course_id, grade):
        pass

    def manage_course_materials(self):
        pass

    def monitor_attendance(self):
        pass

    def communicate_with_students(self, message):
        pass

    def logout(self):
        pass

class Admin(User):
    def __init__(self, user_id, name, email, password, admin_id):
        super().__init__(user_id, name, email, password)
        self.admin_id = admin_id

    def manage_user_accounts(self):
        pass

    def generate_reports(self):
        pass

    def oversee_system_operations(self):
        pass

    def manage_system_settings(self):
        pass

    def create_user_account(self, user_type, *args):
        user_type_lower = user_type.lower()
        if user_type_lower == "student":
            return Student(*args)
        elif user_type_lower == "professor":
            return Professor(*args)
        elif user_type_lower == "operator":
            return Operator(*args)
        elif user_type_lower == "parent":
            return Parent(*args)
        else:
            raise ValueError("Invalid user type")

    def logout(self):
        pass

class Operator(User):
    def __init__(self, user_id, name, email, password, operator_id):
        super().__init__(user_id, name, email, password)
        self.operator_id = operator_id

    def provide_technical_support(self):
        pass

    def maintain_system(self):
        pass

    def logout(self):
        pass

class Parent(User):
    def __init__(self, user_id, name, email, password, children):
        super().__init__(user_id, name, email, password)
        self.children = children

    def view_child_progress(self):
        pass

    def track_child_attendance(self):
        pass

    def view_child_assignments(self):
        pass

    def logout(self):
        pass

class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []
        self.course_materials = None

    def add_student(self, student):
        self.students_enrolled.append(student)

    def remove_student(self, student):
        self.students_enrolled.remove(student)

    def update_course_material(self):
        pass

class Grade:
    def __init__(self, student_id, course_id, letter_grade, numeric_score):
        self.student_id = student_id
        self.course_id = course_id
        self.letter_grade = letter_grade
        self.numeric_score = numeric_score

    def update_grade(self):
        pass

class Attendance:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id
        self.dates_absent = []

    def record_absence(self):
        pass

    def calculate_attendance_rate(self):
        pass

class Assignment:
    def __init__(self, assignment_id, course_id, title, description, deadline):
        self.assignment_id = assignment_id
        self.course_id = course_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.submission_status = None

    def submit_assignment(self):
        pass

    def view_assignment(self):
        pass

class FinancialInformation:
    def __init__(self, student_id, tuition_fees, payment_status):
        self.student_id = student_id
        self.tuition_fees = tuition_fees
        self.payment_status = payment_status

    def view_financial_information(self):
        pass

class Communication:
    def __init__(self, sender_id, receiver_id, message_content, announcement_content, timestamp):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_content = message_content
        self.announcement_content = announcement_content
        self.timestamp = timestamp

    def send_announcement(self):
        pass

    def send_message(self):
        pass

    def view_announcements(self):
        pass

    def view_messages(self):
        pass

class AcademicCalendar:
    def __init__(self, semester, start_date, end_date, holidays, important_dates):
        self.semester = semester
        self.start_date = start_date
        self.end_date = end_date
        self.holidays = holidays
        self.important_dates = important_dates

    def view_academic_calendar(self):
        pass

class Report:
    def __init__(self, report_id, report_type, content, generated_by, timestamp):
        self.report_id = report_id
        self.report_type = report_type
        self.content = content
        self.generated_by = generated_by
        self.timestamp = timestamp

    def generate_report(self):
        pass

class SystemSettings:
    def __init__(self, setting_id, setting_name, setting_value):
        self.setting_id = setting_id
        self.setting_name = setting_name
        self.setting_value = setting_value

    def update_setting(self):
        pass

def main():
    admin = Admin("A1", "Monica", "monica@si.ukrida.ac.id", "adminpass", "admin123")

    student = admin.create_user_account("student", "S1", "Peter", "peter@si.ukrida.ac.id", "studentpass", "E1234")
    professor = admin.create_user_account("professor", "P1", "Dr. Endi", "example@ukrida.ac.id", "profpwd", "F5678")
    operator = admin.create_user_account("Operator", "O1", "operator@example.com", "operatorpass", "operator123")
    parent = admin.create_user_account("parent", "Par1", "parent@example.com", "parentpass", ["child1", "child2"])

    print("User IDs:")
    print("Student ID:", student.get_user_id())
    print("Professor ID:", professor.get_user_id())
    print("Operator ID:", operator.get_user_id())
    print("Parent ID:", parent.get_user_id())

if __name__ == "__main__":
    main()
