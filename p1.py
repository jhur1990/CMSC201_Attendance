"""
File: p1.py
Author: Joshua Hur
Date: 11/03/22
Lab Section: 14
Email: jhur1@umbc.edu
Description: This program shows the lists of students and their class attendance information
with the following criteria;
1. The names of students who have yet to show up.
2. Clock-in and out time for specific students.
3. Clock-in time for all students who attended on time and arrived late to class.
4. The names of students who clocked in the earliest.

"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''


def list_students_not_in_class(class_roster, attendance_list):
    """
    Compare the swipe log with the given course roster. Place those students that
    did not show up for class into a list
    :param class_roster: The list of students who are supposed to attend
    :param attendance_list: The student list and attendance information that structured in the following manner;
    last name, first name, clock-in and out time, and date.
    :return: The list of students who never show up to the class
    """

    temp_list = []
    new_list = []

    STUDENT_NAME_STRING_SLICE = -22

    # Get student's names from the data
    for name in attendance_list:
        temp_list.append(name[:STUDENT_NAME_STRING_SLICE])

    # Compare if student's names are matched to the ones in the class roster
    for name_two in class_roster:
        if name_two not in temp_list:
            new_list.append(name_two)

    return new_list


def list_all_times_checking_in_and_out(student_name, attendance_list):
    """
    Looking at the swiping log, this function will list all in and outs for a
    particular Student. Please note, as coded in the p1.py file given, this
    function was called three times with different student values
    :param student_name: The name of the specific student asked
    :param attendance_list: The student list and attendance information that structured in the following manner;
    last name, first name, clock-in and out time, and date.
    :return: The list of the attendance information of the asked specific student,
    including their last name, first name, clock-in and out time, and date.
    """

    new_list = []

    STUDENT_NAME_STRING_SLICE = -22

    # Look for if there is any check-in and out information for the entered student
    for stu_info in attendance_list:
        if student_name == stu_info[:STUDENT_NAME_STRING_SLICE]:
            new_list.append(stu_info)

    return new_list


def list_all_times_checked_in(attendance_list):
    """
    This function returns a list of when all student(s) FIRST swipe in
    :param attendance_list: The student list and attendance information that structured in the following manner;
    last name, first name, clock-in and out time, and date.
    :return: The list of students and their clock-in times
    """

    temp_list = []
    new_list = []

    START_STRING = 1

    LAST_NAME_INDEX = 0
    FIRST_NAME_INDEX = 1
    TIME_INDEX = 2
    DATE_INDEX = 3

    LIMIT_LIST_LENGTH = 3
    STUDENT_ROTATION = 4

    # Split student attendance data into four types; last name, first name, time, and date
    for stu_data in attendance_list:
        data_split = stu_data.split(",")
        stu_last_name = data_split[LAST_NAME_INDEX]
        stu_first_name = data_split[FIRST_NAME_INDEX][START_STRING:]
        stu_time = data_split[TIME_INDEX][START_STRING:]
        stu_date = data_split[DATE_INDEX][START_STRING:]

        # Only store the first check-in time
        if stu_last_name and stu_first_name not in temp_list:
            temp_list.append(stu_last_name)
            temp_list.append(stu_first_name)
            temp_list.append(stu_time)
            temp_list.append(stu_date)

    # Combine each split student's information
    for new_stu_index in range(len(temp_list) - LIMIT_LIST_LENGTH):
        if new_stu_index % STUDENT_ROTATION == 0:
            restructured_stu_data = temp_list[new_stu_index] + ", " + \
                                    temp_list[new_stu_index + FIRST_NAME_INDEX] + ", " + \
                                    temp_list[new_stu_index + TIME_INDEX] + ", " + \
                                    temp_list[new_stu_index + DATE_INDEX]
            new_list.append(restructured_stu_data)

    return new_list


def list_students_late_to_class(timestamp, attendance_list):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in
    :param timestamp: The input time that wants to be considered as the class start time
    :param attendance_list: The student list and attendance information that structured in the following manner;
    last name, first name, clock-in and out time, and date.
    :return: The list of students who checked in beyond the input time
    """

    temp_list = []
    new_list = []

    START_STRING = 1

    LAST_NAME_INDEX = 0
    FIRST_NAME_INDEX = 1
    TIME_INDEX = 2
    DATE_INDEX = 3

    START_LOOP = 2
    LIMIT_LIST_LENGTH = 1
    STUDENT_ROTATION = 4

    CONV_MIN_TO_SEC = 60

    HOUR_STRING_SLICE = 2
    START_MINUTE_STRING_SLICE = 3
    END_MINUTE_STRING_SLICE = 5
    SEC_STRING_SLICE = 6

    GET_LAST_NAME_INDEX = 2
    GET_FIRST_NAME_INDEX = 1
    GET_DATE_INDEX = 1

    HOUR_INDEX = 0
    MIN_INDEX = 1
    SEC_INDEX = 2

    # Split the input into hours, minutes, and seconds
    comparison_time = timestamp.split(":")

    # Split student attendance data into four types; last name, first name, time, and date
    for stu_data in attendance_list:
        data_split = stu_data.split(",")
        stu_last_name = data_split[LAST_NAME_INDEX]
        stu_first_name = data_split[FIRST_NAME_INDEX][START_STRING:]
        stu_time = data_split[TIME_INDEX][START_STRING:]
        stu_date = data_split[DATE_INDEX][START_STRING:]

        # Only store the first check-in time
        if stu_last_name and stu_first_name not in temp_list:
            temp_list.append(stu_last_name)
            temp_list.append(stu_first_name)
            temp_list.append(stu_time)
            temp_list.append(stu_date)

    # Check any check-in times beyond the input and combine qualified split data
    for stu_index in range(START_LOOP, len(temp_list) - LIMIT_LIST_LENGTH, STUDENT_ROTATION):
        if int(temp_list[stu_index][:HOUR_STRING_SLICE]) >= int(comparison_time[HOUR_INDEX]):
            if int(temp_list[stu_index][START_MINUTE_STRING_SLICE:END_MINUTE_STRING_SLICE] * CONV_MIN_TO_SEC +
                   temp_list[stu_index][SEC_STRING_SLICE:]) > int(comparison_time[MIN_INDEX] * CONV_MIN_TO_SEC +
                                                                  comparison_time[SEC_INDEX]):
                restructured_stu_data = temp_list[stu_index - GET_LAST_NAME_INDEX] + ", " + \
                                        temp_list[stu_index - GET_FIRST_NAME_INDEX] + ", " + \
                                        "".join(temp_list[stu_index]) + ", " + \
                                        temp_list[stu_index + GET_DATE_INDEX]

                new_list.append(restructured_stu_data)

    return new_list


def get_first_student_to_enter(attendance_list):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter
    :param attendance_list: The student list and attendance information that structured in the following manner;
    last name, first name, clock-in and out time, and date.
    :return: The name of the earliest checked-in student
    """
    temp_list = []

    START_STRING = 1

    LAST_NAME_INDEX = 0
    FIRST_NAME_INDEX = 1
    TIME_INDEX = 2
    DATE_INDEX = 3

    CONV_HOUR_TO_MIN = 60
    CONV_MIN_TO_SEC = 60

    HOUR_STRING_SLICE = 2
    START_MINUTE_STRING_SLICE = 3
    END_MINUTE_STRING_SLICE = 5
    SEC_STRING_SLICE = 6

    START_LOOP = 2
    LIMIT_LIST_LENGTH = 1
    STUDENT_ROTATION = 4

    GET_LAST_NAME_INDEX = 2
    GET_FIRST_NAME_INDEX = 1

    earliest_stu = 0

    # Split student attendance data into four types; last name, first name, time, and date
    for stu_data in attendance_list:
        data_split = stu_data.split(",")
        stu_last_name = data_split[LAST_NAME_INDEX]
        stu_first_name = data_split[FIRST_NAME_INDEX][START_STRING:]
        stu_time = data_split[TIME_INDEX][START_STRING:]
        stu_date = data_split[DATE_INDEX][START_STRING:]

        # Only store the first check-in time
        if stu_last_name and stu_first_name not in temp_list:
            temp_list.append(stu_last_name)
            temp_list.append(stu_first_name)
            temp_list.append(stu_time)
            temp_list.append(stu_date)

    # Assign the temporary earliest time for comparison and convert it to seconds
    sample_hour_to_sec = int(temp_list[TIME_INDEX][:HOUR_STRING_SLICE]) * CONV_HOUR_TO_MIN * CONV_MIN_TO_SEC
    sample_min_to_sec = int(temp_list[TIME_INDEX][START_MINUTE_STRING_SLICE:END_MINUTE_STRING_SLICE]) * CONV_MIN_TO_SEC
    sample_sec = int(temp_list[TIME_INDEX][SEC_STRING_SLICE:])

    sample_time = sample_hour_to_sec + sample_min_to_sec + sample_sec

    # Convert every time data to seconds for comparison
    for time_index in range(START_LOOP, len(temp_list) - LIMIT_LIST_LENGTH, STUDENT_ROTATION):

        new_hour_to_sec = int(temp_list[time_index][:HOUR_STRING_SLICE]) * CONV_HOUR_TO_MIN * CONV_MIN_TO_SEC
        new_min_to_sec = int(temp_list[time_index][START_MINUTE_STRING_SLICE:END_MINUTE_STRING_SLICE]) * CONV_MIN_TO_SEC
        new_sec = int(temp_list[time_index][SEC_STRING_SLICE:])

        new_time = new_hour_to_sec + new_min_to_sec + new_sec

        # Compare whichever time is less and move on to the next
        if new_time < sample_time:
            sample_time = new_time
            earliest_stu = temp_list[time_index - GET_LAST_NAME_INDEX] + ", " + \
                           temp_list[time_index - GET_FIRST_NAME_INDEX]

    return earliest_stu


def printList(input_list):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in
    :param input_list: The list of students and their attendance information sent by other functions
    """

    # Print all data
    for print_all in input_list:
        print(print_all)


''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. Nicholas, 9am class

    # load class roster here into a list
    classRoster = fill_roster()

    # figure out which attendance data file to load here

    # load data
    attendData = fill_attendance_data()

    # use different tests
    # make sure roster was filled 
    # printList(classRoster)
    # make sure attendance data was loaded
    # printList(attendData)

    # list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    # list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    # display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    # display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    # display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))


''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
