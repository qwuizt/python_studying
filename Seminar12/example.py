import csv


class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subject_names = next(reader)  # Read the subject names from the first row of the CSV
            for subject_name in subject_names:
                self.subjects[subject_name] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            if 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if 0 <= test_score <= 100:
                self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject in self.subjects:
            test_scores = self.subjects[subject]['test_scores']
            if test_scores:
                return sum(test_scores) / len(test_scores)
            else:
                return 0  # No test scores available
        else:
            return None

    def get_average_grade(self):
        total_grades = []
        for subject_data in self.subjects.values():
            total_grades.extend(subject_data['grades'])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0  # No grades available

    def __setattr__(self, name, value):
        if name == "name":
            if all(c.isalpha() and (c.islower() or c.isupper()) or c.isspace() for c in value):
                super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:

            return None

    def __str__(self):
        for key, value1, value2, value3, value4 in self.subjects:
            if (value1 and value2 and value3 and value4) is not None:
                subject_list = ", ".join(key)
        return f"Студент: {self.name}\nПредметы: {subject_list}"


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)






