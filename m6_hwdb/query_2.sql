SELECT ROUND(AVG(marks.mark), 2) AS avgMarks, students.student, classes.lesson 
FROM marks INNER JOIN students 
ON marks.student_id = students.id
INNER JOIN classes
ON marks.lesson_id = classes.id
WHERE classes.lesson = "Algebra"
GROUP BY students.student
ORDER BY avgMarks DESC LIMIT 1