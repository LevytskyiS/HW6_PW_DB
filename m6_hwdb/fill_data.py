import faker
from datetime import datetime
from random import randint, choice
import sqlite3


NUMBER_OF_STUDENTS = 30
NUMBER_OF_TEACHERS = 4
NUMBER_OF_CLASSES = 7
NUMBER_OF_GROUPS = 3


def generate_data(number_studs, number_teachers, number_groups) -> tuple:

    fake_students = []
    fake_teachers = []
    fake_classes = [
        "Math",
        "History",
        "Arts",
        "Literature",
        "Biology",
        "Algebra",
        "Chemistry ",
    ]
    fake_groups = []
    fake_marks = [1, 2, 3, 4, 5]
    fake_data = faker.Faker()

    for _ in range(number_studs):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.bothify(text="??-##"))

    return fake_students, fake_teachers, fake_classes, fake_groups, fake_marks


def prepare_data(students, teachers, classes, groups, marks) -> tuple:

    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_OF_GROUPS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_classes = []
    for lesson in classes:
        for_classes.append((lesson, randint(1, NUMBER_OF_TEACHERS)))

    for_groups = []
    for one_group in groups:
        for_groups.append((one_group,))

    for_marks = []
    for student in students:
        for _ in range(5):
            mark_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            for_marks.append(
                (
                    randint(1, NUMBER_OF_CLASSES),
                    students.index(student) + 1,
                    choice(marks),
                    mark_date,
                )
            )

    return for_students, for_teachers, for_classes, for_groups, for_marks


def insert_data_to_db(students, teachers, classes, groups, mark) -> None:

    with sqlite3.connect("university.db") as con:

        cur = con.cursor()

        sql_to_teachers = """
        INSERT INTO teachers (teacher)
        VALUES (?)
        """
        cur.executemany(sql_to_teachers, teachers)

        sql_to_classes = """
        INSERT INTO classes (lesson, teacher_id)
        VALUES (?, ?)
        """
        cur.executemany(sql_to_classes, classes)

        sql_to_groups = """
        INSERT INTO groups (group_name)
        VALUES (?)
        """
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """
        INSERT INTO students (student, group_id)
        VALUES (?, ?)
        """
        cur.executemany(sql_to_students, students)

        sql_to_marks = """
        INSERT INTO marks (lesson_id, student_id, mark, created_at)
        VALUES (?, ?, ?, ?)
        """
        cur.executemany(sql_to_marks, mark)

        con.commit()


if __name__ == "__main__":
    students, teachers, classes, groups, marks = prepare_data(
        *generate_data(
            NUMBER_OF_STUDENTS,
            NUMBER_OF_TEACHERS,
            NUMBER_OF_GROUPS,
        )
    )
    insert_data_to_db(students, teachers, classes, groups, marks)
