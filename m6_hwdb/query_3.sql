SELECT ROUND(AVG(marks.mark), 2) AS avgMarks, groups.group_name, classes.lesson
FROM marks INNER JOIN classes
ON marks.lesson_id = classes.id 
INNER JOIN students
ON marks.student_id = students.id 
INNER JOIN groups
ON students.group_id = groups.id
WHERE groups.group_name = "AZ-59" AND classes.lesson = "Math"