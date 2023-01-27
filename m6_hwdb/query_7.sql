SELECT groups.group_name, students.student, marks.mark, classes.lesson 
FROM marks INNER JOIN students
ON marks.student_id = students.id
INNER JOIN groups
ON students.group_id = groups.id
INNER JOIN classes
ON marks.lesson_id = classes.id 
WHERE groups.group_name = "is-13" AND classes.lesson = "Chemistry "
ORDER BY students.student 