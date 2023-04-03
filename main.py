grade = [('Англійська мова', 88), ('Біологія', 90), ('Математика', 97), ('Українська мова', 82)]

def take_second(elem):
    return elem[1]

take_second(grade)

grade.sort(key = take_second)

print(list(reversed(grade)))