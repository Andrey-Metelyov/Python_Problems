# the list "students" is already defined

# students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]

print([name for name, grade in students if grade == 'A'])
