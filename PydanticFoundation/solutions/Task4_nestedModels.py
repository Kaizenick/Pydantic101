from typing import List, Optional
from pydantic import BaseModel

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lesson(BaseModel):
    lesson_number: int
    lesson_name: str

class Module(BaseModel):
    module_number: int
    lessons: List[Lesson]

class Course(BaseModel):
    course_name: str
    modules: List[Module]

l1 = Lesson(lesson_number=1,lesson_name="lesson1")
l2 = Lesson(lesson_number=2,lesson_name="lesson2")
l3 = Lesson(lesson_number=3,lesson_name="lesson3")
l4 = Lesson(lesson_number=4,lesson_name="lesson4")

m1 = Module(module_number=1,lessons=[l1,l2])
m2 = Module(module_number=2,lessons=[l3,l4])

c1 = Course(course_name="course1", modules=[m1,m2])

print(c1)
