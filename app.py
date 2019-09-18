from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    roster = [Student("John", 90),
              Student("Bob", 70),
              Student("Amanda", 85),
              Student("Sara", 100),
              Student("Amy", 65),
              Student("Oliver", 79),
              Student("Barry", 45),
              Student("Jay", 80),
              Student("Carey", 65),
              Student("Jax", 98)]

    for i in roster:
        i.print_student_info()

    print(average_grade(roster))

__main__()
