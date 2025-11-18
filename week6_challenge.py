module_prerequisites={"CIS1702":[],"CIS1000":["CIS1702"],"CIS1001":["CIS1702"],"CIS2000":["CIS1702","CIS1000"],"MTH1001":[],"CIS2005":["MTH1001","CIS1000"]}
student_info={"Alice":["CIS1702","MTH1001"],"Bob":["CIS1702","CIS1001"],"Charlie":["MTH1001"]}
student_database={"s12345":student_info["Alice"],"s67890":student_info["Bob"],"s54321":student_info["Charlie"]}

def can_enroll(student_id,module_code):
    all_good=True
    if student_id in student_database:
        if module_code in module_prerequisites:
            prerequisite_list=module_prerequisites[module_code]
            completed_module_list=student_database[student_id]
            completed_set=set(completed_module_list)
            
            if module_code in completed_set:
                all_good=False
                print("This student has already completed that module.")
            else:

                for i in range(len(prerequisite_list)):
                    if(prerequisite_list[i] in completed_set):
                        all_good=all_good #Sorry, this is kinda terrible but I couldn't be bothered to make my if statement the other way round. This line is just to prove there's something in the if block even though it doens't do anything.
                    else:
                        all_good=False
                        print(f"This student must complete {prerequisite_list[i]}")
        else:
            print("Sorry, that module was not found.")
    else:
        print("Sorry, that student was not found.")
    
    return all_good

def enroll_student(student_id,module_code):
    if can_enroll(student_id,module_code)==True:
        print("Student enrolled!")
        student_database[student_id].append(module_code)
    else:
        "Enrollment Failed."


enroll_student("s54321","CIS1000") #Fails
enroll_student("s12345","CIS1000") #Succeeds
enroll_student("s12345","CIS1000") #Fails
enroll_student("s12345","CIS2000") #Succeeds