SELECT  teachers.teacher, classes.lesson
FROM classes INNER JOIN teachers
ON classes.teacher_id = teachers.id
WHERE teachers.teacher = "Virginia Andrade"