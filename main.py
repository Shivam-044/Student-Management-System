class Student:
    """Represents a student in the system."""
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Marks: {self.marks}"

    def display(self):
        print(f"\n--- Student Record ---")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Marks      : {self.marks}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def _get_valid_input(self, prompt, data_type):
        """Helper to handle input errors."""
        while True:
            try:
                return data_type(input(prompt))
            except ValueError:
                print(f"Invalid input. Please enter a valid {data_type.__name__}.")

    def add_student(self):
        s_id = self._get_valid_input("Enter Student ID: ", int)
        name = input("Enter Student Name: ")
        age = self._get_valid_input("Enter Age: ", int)
        marks = self._get_valid_input("Enter Marks: ", float)
        
        self.students.append(Student(s_id, name, age, marks))
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students registered.")
            return
        for student in self.students:
            student.display()

    def search_student(self):
        s_id = self._get_valid_input("Enter Student ID to Search: ", int)
        for s in self.students:
            if s.student_id == s_id:
                s.display()
                return
        print("Student not found.")

    def update_marks(self):
        s_id = self._get_valid_input("Enter Student ID: ", int)
        for s in self.students:
            if s.student_id == s_id:
                s.marks = self._get_valid_input("Enter New Marks: ", float)
                print("Marks updated successfully!")
                return
        print("Student not found.")

    def delete_student(self):
        s_id = self._get_valid_input("Enter Student ID: ", int)
        for i, s in enumerate(self.students):
            if s.student_id == s_id:
                del self.students[i]
                print("Student deleted successfully!")
                return
        print("Student not found.")

    def display_topper(self):
        if not self.students:
            print("No students available.")
            return
        topper = max(self.students, key=lambda s: s.marks)
        print("\n=== TOPPER DETAILS ===")
        topper.display()

def main():
    sms = StudentManagementSystem()
    menu = {
        "1": sms.add_student,
        "2": sms.view_students,
        "3": sms.search_student,
        "4": sms.update_marks,
        "5": sms.delete_student,
        "6": sms.display_topper,
        "7": exit
    }

    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student\n2. View All\n3. Search\n4. Update Marks\n5. Delete\n6. Topper\n7. Exit")
        choice = input("Select an option: ")
        
        if choice == "7":
            print("Exiting...")
            break
        
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()