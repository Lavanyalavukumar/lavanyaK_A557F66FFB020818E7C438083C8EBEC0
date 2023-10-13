"""
Implement a function called sort_studnts that takes a list of stundent objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function 
with different input lists of students. 
"""

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(students_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(students_list, 
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Lavanya", "A123", 7.8),
    Student("Bruntha", "A124", 8.9),
    Student("Sarathi", "A125", 9.1),
    Student("Kaviya", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,

student.roll_number,
                                                     student.cgpa))