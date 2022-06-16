def ask_student_course():
    it_courses = []

    while True:
        ask_student_for_course = str(input("Enter in course name: "))

        it_courses.append(ask_student_for_course)

        ask_again = input("Do you want to enter another course name Y/N:").upper()
        if ask_again == "N":
            break

    it_courses.sort()

    file_ptr = open("courses.txt", "w")

    for course in it_courses:
        file_ptr.write(course + "\n")

    file_ptr.close()


ask_student_course()


