# GOOD EVENING, EVERYONE!
# THIS IS MY WEEK 2 ASSIGNMENT.
# HOPE I DID WELL.
#######################################################CONTACT_BOOK#######################################################
import sys

contacts = []

# test_dummy = {
#     "S/N" : ,
#     "first_name" : ,
#     "last_name" : ,
#     "phone" : ,
#     "e-mail" :
# }


#####################################################################################################################################################################
#######################################################CREATE_CONTACTS#######################################################
def create_contacts_l_1():
    def create_contacts_l_2(
        serial_number, first_name, last_name, phone, e_mail, creating
    ):
        stack = {
            "S/N": serial_number,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "e-mail": e_mail,
        }

        creating.append(stack)
        return stack

    create_contacts_l_2(
        int(input("Enter the index number starting from '0' to ...: ")),
        input("Enter the First Name: "),
        input("Enter the Last Name: "),
        input("Enter the Phone: "),
        input("Enter the E-mail Address: "),
        contacts,
    )


def confirm_create_1():
    confirm_1_1 = input("Do you want to create another contact? ")
    if confirm_1_1.lower() == "yes":
        create_contacts_l_1()
    elif confirm_1_1.lower() == "no":
        print("Moving on!\n")
        confirm_create_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_create_1()


def confirm_create_2():
    confirm_1_2 = input(
        "What do you want to do next?\n1 - 'Read Contacts'\n2 - 'Update Contacts'\n3 - 'Delete Contact'\n4 - 'Exit System'!\n"
    )
    if confirm_1_2 == "1":
        read_contacts()
    elif confirm_1_2 == "2":
        update_contacts_l_1()
    elif confirm_1_2 == "3":
        delete_contacts()
    elif confirm_1_2 == "4":
        sys.exit()
    else:
        print("Please Enter a valid input!")
        confirm_create_2()


#####################################################################################################################################################################
#######################################################READ_CONTACTS#######################################################
def read_contacts():
    print(contacts)


def confirm_read_1():
    confirm_2_1 = input(
        "What do you want to do next?\n1 - 'Create Contacts'\n2 - 'Update Contacts'\n3 - 'Delete Contact'\n4 - 'Exit System'!\n"
    )
    if confirm_2_1 == "1":
        create_contacts_l_1()
    elif confirm_2_1 == "2":
        update_contacts_l_1()
    elif confirm_2_1 == "3":
        delete_contacts()
    elif confirm_2_1 == "4":
        sys.exit()
    else:
        print("Please Enter a valid input!")
        confirm_read_1()


#####################################################################################################################################################################
#######################################################UPDATE_CONTACTS#######################################################
def update_contacts_l_1():
    asking = int(input("Enter the index of the contact which you want to update: "))
    temp = contacts[asking]
    print(temp)

    def update_contacts_l_2():
        asking_2 = int(
            input(
                "What are you updating? 1 'Serial Number', 2 'First Name', 3 'Last Name', 4 'Phone', & 5 'E-mail': "
            )
        )

        if asking_2 == 1:
            temp[0] = input("Enter/Update the Serial Number: ")
            print(temp)
            print(contacts)
        elif asking_2 == 2:
            temp[1] = input("Enter/Update the First Name: ")
            print(temp)
            print(contacts)
        elif asking_2 == 3:
            temp[2] = input("Enter/Update the Last Name: ")
            print(temp)
            print(contacts)
        elif asking_2 == 4:
            temp[3] = input("Enter/Update the Phone: ")
            print(temp)
            print(contacts)
        elif asking_2 == 5:
            temp[4] = input("Enter/Update the E-mail: ")
            print(temp)
            print(contacts)
        else:
            print("Please enter a valid input 'Between 1 & 5'!\n")
            update_contacts_l_2()

    update_contacts_l_2()


def confirm_update_1():
    confirm_3_1 = input("Do you want to update another contact? ")
    if confirm_3_1.lower() == "yes":
        update_contacts_l_1()
    elif confirm_3_1.lower() == "no":
        print("Moving on!\n")
        confirm_update_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_create_1()


def confirm_update_2():
    confirm_3_2 = input(
        "What do you want to do next?\n1 - 'Create Contacts'\n2 - 'Read Contacts'\n3 - 'Delete Contact'\n4 - 'Exit System'!\n"
    )
    if confirm_3_2 == "1":
        create_contacts_l_1()
    elif confirm_3_2 == "2":
        read_contacts()
    elif confirm_3_2 == "3":
        delete_contacts()
    elif confirm_3_2 == "4":
        sys.exit()
    else:
        print("Please Enter a valid input!")
        confirm_update_2()


#####################################################################################################################################################################
#######################################################DELETE_CONTACTS#######################################################
def delete_contacts():
    ask = int(input("Enter the index of the contact you want to delete: "))
    del contacts[ask]


def confirm_delete_1():
    confirm_4_1 = input("Do you want to delete another contact? ")
    if confirm_4_1.lower() == "yes":
        delete_contacts()
    elif confirm_4_1.lower() == "no":
        print("Moving on!\n")
        confirm_delete_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_delete_1()


def confirm_delete_2():
    confirm_4_2 = input(
        "What do you want to do next?\n1 - 'Create Contacts'\n2 - 'Read Contacts'\n3 - 'Update Contact'\n4 - 'Exit System'!\n"
    )
    if confirm_4_2 == "1":
        create_contacts_l_1()
    elif confirm_4_2 == "2":
        read_contacts()
    elif confirm_4_2 == "3":
        update_contacts_l_1()
    elif confirm_4_2 == "4":
        sys.exit()
    else:
        print("Please Enter a valid input!")
        confirm_delete_2()


#####################################################################################################################################################################
#######################################################ACTUAL_IMPLEMENTATION_OF_CONTACT_BOOK#######################################################
def contact_book():
    print("Welcome to the Contact Book!")
    select = input(
        "Select an Operation!\n1 for 'Creating Contact'\n2 for 'Reading Contacts'\n3 for 'Updating Contacts' &\n4 for 'Deleting Contacts'!\n"
    )
    if select == "1":
        create_contacts_l_1()
        confirm_create_1()
    elif select == "2":
        read_contacts()
        confirm_read_1()
    elif select == "3":
        update_contacts_l_1()
        confirm_update_1()
    elif select == "4":
        delete_contacts()
        confirm_delete_1()
    else:
        print("Enter a valid input!\n")
        contact_book()


#######################################################TASK_MANAGER#######################################################

task_list = []


#####################################################################################################################################################################
#######################################################CREATE_TASK#######################################################
def create_task_l_1(arrange):
    def create_task():
        queue = input("Add a new list...\n")

        arrange.append(queue)

    create_task()
    print(task_list)


def reassure_create_list_1():
    reassuring_1_1 = input("Do you want to add another list?\n")
    if reassuring_1_1.lower() == "yes":
        create_task_l_1(task_list)
        reassure_create_list_1()
    elif reassuring_1_1.lower() == "no":
        reassure_create_list_2()
    else:
        print("Please, enter a 'yes' or 'no'!")
        reassure_create_list_1()


def reassure_create_list_2():
    reassuring_1_2 = input("Do you want to perform another function?\n")
    if reassuring_1_2.lower() == "yes":

        def affirmative_1():
            affirm = input(
                "What do you want to do next?\n1 - 'Create List'\n2 - 'Read List'\n3 - 'Update A List'\n4 - 'Delete A List'\n5 - 'Exit System'!\n"
            )
            if affirm == "1":
                create_task_l_1(task_list)
            elif affirm == "2":
                read_task()
            elif affirm == "3":
                update_task()
            elif affirm == "4":
                delete_task()
            elif affirm == "5":
                sys.exit()
            else:
                print("Please, enter a valid input!\n")
                affirmative_1()

        affirmative_1()
        reassure_create_list_2()
    elif reassuring_1_2.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("Please, enter a 'yes' or 'no'!")
        reassure_create_list_2()


#####################################################################################################################################################################
#######################################################READ_TASK#######################################################
def read_task():
    print(task_list)


def reassure_read_list():
    reassuring_2_1 = input("Do you want to perform another function?\n")
    if reassuring_2_1.lower() == "yes":

        def affirmative_2():
            affirm = input(
                "What do you want to do next?\n1 - 'Create List'\n2 - 'Read List'\n3 - 'Update A List'\n4 - 'Delete A List'\n5 - 'Exit System'!\n"
            )
            if affirm == "1":
                create_task_l_1(task_list)
            elif affirm == "2":
                read_task()
            elif affirm == "3":
                update_task()
            elif affirm == "4":
                delete_task()
            elif affirm == "5":
                sys.exit()
            else:
                print("Please, enter a valid input!\n")
                affirmative_2()

        affirmative_2()
        reassure_read_list()
    elif reassuring_2_1.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("Please, enter a 'yes' or 'no'!")
        reassure_read_list()


#####################################################################################################################################################################
#######################################################UPDATE_TASK#######################################################
def update_task():
    indexing = int(
        input(
            "Enter the index of the list you want to Update 'Note, indexing in a list starts from 0!': "
        )
    )
    task_list[indexing] = input("Enter/Update the list\n")
    print(task_list)


def reassure_update_list_1():
    reassuring_3_1 = input("Do you want to update another list?\n")
    if reassuring_3_1.lower() == "yes":
        update_task()
        reassure_update_list_1()
    elif reassuring_3_1.lower() == "no":
        reassure_update_list_2()
    else:
        print("\nPlease, enter a 'yes' or 'no'!\n")
        reassure_read_list()


def reassure_update_list_2():
    reassuring_3_2 = input("Do you want to perform another function?\n")
    if reassuring_3_2.lower() == "yes":

        def affirmative_3():
            affirm = input(
                "What do you want to do next?\n1 - 'Create List'\n2 - 'Read List'\n3 - 'Update A List'\n4 - 'Delete A List'\n5 - 'Exit System'!\n"
            )
            if affirm == "1":
                create_task_l_1(task_list)
            elif affirm == "2":
                read_task()
            elif affirm == "3":
                update_task()
            elif affirm == "4":
                delete_task()
            elif affirm == "5":
                sys.exit()
            else:
                print("Please, enter a valid input!\n")
                affirmative_3()

        affirmative_3()
        reassure_update_list_2()
    elif reassuring_3_2.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("\nPlease, enter a 'yes' or 'no'!\n")
        reassure_update_list_2()


#####################################################################################################################################################################
#######################################################DELETE_TASK#######################################################
def delete_task():
    deleting = int(input("Enter the index of the list you want to delete/check: "))
    del task_list[deleting]
    print(task_list)


def reassure_delete_list_1():
    reassuring_4_1 = input("Do you want to delete another list?\n")
    if reassuring_4_1.lower() == "yes":
        delete_task()
        reassure_delete_list_1()
    elif reassuring_4_1.lower() == "no":
        reassure_delete_list_2()
    else:
        print("\nPlease, enter a 'yes' or 'no'!\n")
        reassure_delete_list_1()


def reassure_delete_list_2():
    reassuring_4_2 = input("Do you want to perform another function?\n")
    if reassuring_4_2.lower() == "yes":

        def affirmative_4():
            affirm = input(
                "What do you want to do next?\n1 - 'Create List'\n2 - 'Read List'\n3 - 'Update A List'\n4 - 'Delete A List'\n5 - 'Exit System'!\n"
            )
            if affirm == "1":
                create_task_l_1(task_list)
            elif affirm == "2":
                read_task()
            elif affirm == "3":
                update_task()
            elif affirm == "4":
                delete_task()
            elif affirm == "5":
                sys.exit()
            else:
                print("Please, enter a valid input!\n")
                affirmative_4()

        affirmative_4()
        reassure_delete_list_2()
    elif reassuring_4_2.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("\nPlease, enter a 'yes' or 'no'!\n")
        reassure_delete_list_2()


#####################################################################################################################################################################
#######################################################ACTUAL_IMPLEMENTATION_OF_TASK_MANAGER#######################################################
def task_manager():
    first = input(
        "Enter...\n1 to 'Create A List'\n2 to 'Read All Lists'\n3 to 'Update A List' &\n4 to 'Delete/Check List'!\n"
    )
    if first == "1":
        create_task_l_1(task_list)
        reassure_create_list_1()
        reassure_create_list_2()
    elif first == "2":
        read_task()
        reassure_read_list()
    elif first == "3":
        update_task()
        reassure_update_list_1()
        reassure_update_list_2()
    elif first == "4":
        delete_task()
        reassure_delete_list_1()
        reassure_delete_list_2()
    else:
        print("Please, enter a valid input!\n")
        task_manager()
#####################################################################################################################################################################
#######################################################ADDED_IMPLEMENTATIONS#######################################################
def repetition_1():
    rep_1 = input("Do you want to launch the Task Manager?\n") 
    if rep_1.lower() == "yes":
        task_manager()
    elif rep_1.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        repetition_1()

def repetition_2():
    rep_2 = input("Do you want to launch the Contact Book?\n")
    if rep_2.lower() == "yes":
        contact_book()
    elif rep_2.lower() == "no":
        print("\nThank you for using ContactTaskBookManager!\n")
        sys.exit()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        repetition_2()

#######################################################CONTACT_TASK_BOOK_MANAGER#######################################################
def ContactTaskBookManager():
    print("Welcome to the ContactTaskBookManager!")
    ask_1 = input("What do you want to do? Press 1 for 'Contact Book' & 2 for 'Task Manager'!\n")
    if ask_1 == "1":
        contact_book()
        repetition_1()
    elif ask_1 == "2":
        task_manager()
        repetition_2()
    else:
        print("Please, enter a valid input!\n")
        ContactTaskBookManager()

ContactTaskBookManager()