class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while i < len(students) and len(students) != 0:
            if (students[0]) != sandwiches[0]:
                students.append(students.pop(0)) # loop
                i = i + 1
            else:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
        return len(students)
