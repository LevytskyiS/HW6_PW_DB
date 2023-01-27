SELECT teachers.teacher, students.student, classes.lesson
FROM marks INNER JOIN classes
ON marks.lesson_id = classes.id 
INNER JOIN students
ON marks.student_id = students.id
INNER JOIN teachers
ON classes.teacher_id = teachers.id
WHERE teachers.teacher = "Donald Norton" AND students.student = "Juan Williams"