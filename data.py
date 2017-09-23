from random import *
import string
"""
This module should use random module to generate_id
"""


def import_data_from_file(filename='class_data.txt'):
    """
    Import data from file to list. Expected returned data format:
        [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
        ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61'],
        ...]

    :param str filename: optional, name of file to be imported

    :returns: list of lists representing students' data
    :rtype: list
    """
    with open(filename, 'r') as filename:
        students = filename.readlines()
        students = [data.rstrip() for data in students]
        students = [data.split(',') for data in students]
    return students


def export_to_file(data, filename='class_data.txt', mode='a'):
    """
    Export data from list to file. If called with mode 'w' it should overwritte
    data in file. If called with mode 'a' it should append data at the end.

    :param list data: students' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    data = str(data)
    
    if mode == 'a':
        with open(filename, 'a') as filename:
            filename.write(data)
    elif mode == 'w':
        with open(filename, 'w') as filename:
            filename.write(data)
    else:
        raise ValueError('Wrong write mode')


def get_student_by_id(uid, students):
    """
    Get student by unique id

    :param str uid: student unique id
    :param list students: students' data

    :raises ValueError: if student's uid not found in class data.
        Error message: 'Student does not exist'

    :returns: specific student's data
    :rtype: list
    """
    uid_index = 0

    for data in students:
        if data[uid_index] == uid:
            return data
        else:
            raise ValueError('Student does not exist')


def get_students_of_class(students, class_name):
    """
    Get all students from given class

    :param list students: list of nested list imported from file
    :param str class_name: string representing class name that student\
        attends to

    :returns: students from given class only
    :rtype: list
    """
    class_index = 4
    class_list = []

    for data in students:
        if data[class_index] == class_name:
            class_list.append(data)
    
    return class_list


def get_youngest_student(students):
    """
    Get youngest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: youngest student
    :rtype: list
    """
    age_index = 3
    youngest_student_age = 0
    youngest_student = []

    for data in students:
        try:
            data[age_index] = int(data[age_index])
            if youngest_student_age == 0:
                youngest_student_age = data[age_index]
            elif data[age_index] >= youngest_student_age:
                youngest_student_age = data[age_index]
                data[age_index] = str(data[age_index])
                youngest_student.append(data)
        except TypeError:
            pass

    youngest_student = youngest_student[-1]
    return youngest_student


def get_youngest_student_of_class(students, class_name):
    """
    Get youngest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: youngest student from given class
    :rtype: list
    """
    age_index = 3
    class_index = 4
    youngest_student_age = 0
    youngest_student_of_class = []

    for data in students:
        try:
            data[age_index] = int(data[age_index])
            if youngest_student_age == 0:
                youngest_student_age = data[age_index]
            elif data[age_index] >= youngest_student_age and data[class_index] == class_name:
                youngest_student_age = data[age_index]
                data[age_index] = str(data[age_index])
                youngest_student_of_class.append(data)
        except TypeError:
            pass

    youngest_student_of_class = youngest_student_of_class[-1]
    return youngest_student_of_class


def get_oldest_student(students):
    """
    Get oldest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: oldest student
    :rtype: list
    """
    age_index = 3
    youngest_student_age = 0
    youngest_student = []

    for data in students:
        try:
            data[age_index] = int(data[age_index])
            if youngest_student_age == 0:
                youngest_student_age = data[age_index]
            elif data[age_index] <= youngest_student_age:
                youngest_student_age = data[age_index]
                data[age_index] = str(data[age_index])
                youngest_student.append(data)
        except TypeError:
            pass

    youngest_student = youngest_student[-1]
    return youngest_student


def get_oldest_student_of_class(students, class_name):
    """
    Get oldest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: oldest student
    :rtype: list
    """
    age_index = 3
    class_index = 4
    youngest_student_age = 0
    youngest_student_of_class = []

    for data in students:
        try:
            data[age_index] = int(data[age_index])
            if youngest_student_age == 0:
                youngest_student_age = data[age_index]
            elif data[age_index] <= youngest_student_age and data[class_index] == class_name:
                youngest_student_age = data[age_index]
                data[age_index] = str(data[age_index])
                youngest_student_of_class.append(data)
        except TypeError:
            pass

    youngest_student_of_class = youngest_student_of_class[-1]
    return youngest_student_of_class


def get_average_grade_of_students(students):
    """
    Calculate average grade of all students

    IMPORTANT:
        Implement this function without built-in functions like sum()
        or similar

    :param list students:  students' data

    :returns: average grade of students value
    :rtype: float
    """
    average_grade_index = 5
    average_grade_total = 0
    total_number_of_students = 0
    result = 0

    for data in students:
        try:
            data[average_grade_index] = float(data[average_grade_index])
            average_grade_total += data[average_grade_index]
            total_number_of_students += 1
        except TypeError:
            pass

    result = average_grade_total / total_number_of_students
    return result


def get_average_presence_of_students(students):
    """
    Returns rounded average presence of all students. For instance,
    if average presence is 35.4912, returned value should be 35,
    if average presence is 41.5, returned value should be 42,

    IMPORTANT:
        Implement this function without built-in functions like sum(), round()
        or similar

    :param list students:  students' data

    :returns: average presence of students rounded to int
    :rtype: int
    """
    average_presence_index = 6
    average_presence_total = 0
    total_number_of_students = 0
    result = 0

    for data in students:
        try:
            data[average_presence_index] = int(data[average_presence_index])
            average_presence_total += data[average_presence_index]
            total_number_of_students += 1
        except TypeError:
            pass

    result = average_presence_total / total_number_of_students
    return result


def generate_id(current_ids):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Generate unique id. It should be unique in all existing students list. If
    generated id was already used, function should regenerate it untill it is
    totaly new. Newly generated unique id should be added to current_ids

    REQUIREMENTS:
        - All ids must be 4-characters long
        - Characters should appear in given order:
            1. Upper letter
            2. Digit from 0 to 9
            3. Special character from this list: !@#$%^&*()_+
            4. Lower letter

            Example ids:
                W1&p
                M9@p
                P1!n

    :param list current_ids: list of all ids. It's used to check if
            generated id is unique or not. If new id is unique, current_ids
            should be extended to include this new id.

    :returns: unique id
    :rtype: str
    """
    
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+'

    while True:
        first_character = "".join(choice(uppercase_characters) for char in range(1))
        second_character = "".join(choice(digits) for char in range(1))
        third_character = "".join(choice(special_characters) for char in range(1))
        fourth_character = "".join(choice(lowercase_characters) for char in range(1))
        unique_id = first_character + second_character + third_character + fourth_character
        if unique_id not in current_ids:
            current_ids.append(unique_id)
            return unique_id
        else:
            continue


def get_all_by_gender(students, gender):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Get all students with given gender. As someone forgot to ask students about
    it, the only way JERZYBOT can find out if someone is female is her name.
    Treat all students with name ending with 'a' as female (Maria, Anna, etc).
    (we're sorry Miriam, we'll update JERZYBOT as soon as possible)

    :param list students:  students' data
    :param str gender: gender to filter by. 'female' will return female
        students, 'male' will return list of male students

    :raises ValueError: if gender other than 'female' or 'male' was given.
        Error message: 'Wrong gender'

    :returns: list of students filtered by given gender
    :rtype: list
    """
    students_by_gender = []
    first_name_index = 1

    for data in students:
        if gender == 'female':
            if data[first_name_index][-1] == 'a':
                students_by_gender.append(data)
            else:
                continue
        elif gender == 'male':
            if data[first_name_index][-1] != 'a':
                students_by_gender.append(data)
        else:
            raise ValueError('Wrong gender')

    return students_by_gender


def sort_students_by_age(students, order=None):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Sorts student list by age. User can choose sorting order by passing
    'desc' for descending order or 'asc' for ascening order.
    If order is None returns empty list

    IMPORTANT:
        Implement this function without using sorted() or similar built-in
        functions

    :param list students:  students' data
    :param str order: optional, sorting order

    :raises ValueError: if order other than 'asc', 'desc' or None
        was given

    :returns: sorted students or empty list
    :rtype: list
    """
