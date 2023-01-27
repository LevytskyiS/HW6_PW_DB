SELECT students.student, classes.lesson 
FROM marks INNER JOIN students
ON marks.student_id = students.id
INNER JOIN classes
ON marks.lesson_id = classes.id
WHERE students.student = "Lisa Lynch"