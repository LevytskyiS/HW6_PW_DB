SELECT groups.group_name, students.student
FROM students INNER JOIN groups
ON students.group_id = groups.id
WHERE groups.group_name = "sG-94"
