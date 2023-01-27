SELECT ROUND(AVG(marks.mark), 2) AS avgMark, teachers.teacher 
FROM marks INNER JOIN classes
ON marks.lesson_id = classes.id
INNER JOIN teachers
ON classes.teacher_id = teachers.id
WHERE teachers.teacher = "Veronica Bates"