SELECT ROUND(AVG(marks.mark), 2) AS avgMarks, students.student
FROM marks INNER JOIN students 
ON marks.student_id = students.id
GROUP BY students.student
ORDER BY avgMarks DESC LIMIT 5
