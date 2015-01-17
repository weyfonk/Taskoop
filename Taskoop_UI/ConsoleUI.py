from Taskoop_Bll import Schedule, StringUtils
from datetime import date, datetime
import string

def Start():
    DisplayWelcomeMessage()
    
    currentSchedule = Schedule.Schedule()
    SetPeopleNb(currentSchedule)
    SetPeopleNames(currentSchedule)
    SetTaskNb(currentSchedule)
    SetTaskNames(currentSchedule)
    SetDates(currentSchedule)
    SetOrientation(currentSchedule)
    currentSchedule.GenerateHTML()
    

def DisplayWelcomeMessage():
    print('----- Welcome to Taskoop!----- \n Press \'q\' to quit.')


# Set time-related data
def SetDates(schedule):
    userInput = string.whitespace
    while not StringUtils.IsDateIncrementInputValid(userInput):
        userInput = input("""How often should the tasks be performed ?
        Every hour [{0}] / day [{1}] / week [{2}]
        / month [{3}] ?""".format(StringUtils.HOUR_KEY,
                                  StringUtils.DAY_KEY,
                                  StringUtils.WEEK_KEY,
                                  StringUtils.MONTH_KEY))
    frequency = userInput.upper()
    startingPoint = -1
    if frequency == StringUtils.HOUR_KEY:
        userInput = string.whitespace
        while not StringUtils.IsHourInputValid(userInput):
            userInput = input("""At what time should the timetable start ?
(Please type a number between 0 and 23) \n""")
        schedule.startingPoint = int(userInput)
    elif frequency == StringUtils.DAY_KEY:
        schedule.startingPoint = date.today()
        #TODO enable other start day than today
        print("Oops... not implemented yet!")
    elif frequency == StringUtils.WEEK_KEY:
        while not StringUtils.IsDateInputValid(userInput):
            userInput = input("""What date should the timetable start ?
(Please type a date in format dd/mm/yyyy) \n""")
        dateMembers = userInput.split('/')
        day = dateMembers[0]
        month = dateMembers[1]
        year = dateMembers[2]
        schedule.startingPoint = date(int(year),int(month),int(day))
    else:
        #TODO
        print("Oops... not implemented yet!")
    schedule.frequency = frequency


# Decide the table orientation if tasks amount and people number are equal
def SetOrientation(schedule):
    userInput = string.whitespace
    if(schedule.taskNb == schedule.peopleNb):
        while not StringUtils.IsYesNoInputValid(userInput):
            userInput = input("""Should the tasks be shown in the table
                 header row ?\n If you answer 'N', it will contain
                 people names. [Y/N]""")
        schedule.arePeopleShownInHeader = userInput.upper() == 'N'
    else:
        schedule.arePeopleShownInHeader = schedule.peopleNb > schedule.taskNb


# Sets the number of participants
def SetPeopleNb(schedule):
    userInput = string.whitespace
    peopleNb = 0
    print('How many people are taking part in this ?')
    while peopleNb == 0 and StringUtils.IsInputValid(userInput):
        userInput = input()
        if userInput.isdigit():
            peopleNb = int(userInput)
            print('OK:', peopleNb, 'people involved.')
        else:
            print('Please type a positive integer')
    schedule.peopleNb = peopleNb


# Sets the participants' names
def SetPeopleNames(schedule):
    userInput = string.whitespace
    people = []
    nbPeople = schedule.peopleNb
    while len(people) < nbPeople and StringUtils.IsInputValid(userInput):
        userInput = input('Please type the name of participant #'
                                        + str(len(people) + 1) + "\n")
        people.append(userInput)
    schedule.people = people

# Sets the number of tasks
def SetTaskNb(schedule):
    userInput = string.whitespace
    tasksNb = 0
    print('How many tasks are to be performed ?')
    while tasksNb == 0 and StringUtils.IsInputValid(userInput):
        userInput = input()
        if userInput.isdigit():
            tasksNb = int(userInput)
            #if tasksNb > peopleNb:
                #print("Too many tasks.",
                #"\nPlease choose at most as many tasks as the number",
                #" of people involved.")
                #tasksNb = 0
            #else:
                #print('OK:', tasksNb, 'tasks.')
        else:
            print('Please type a positive integer')
    schedule.taskNb = tasksNb
    
    
# Set the tasks names
def SetTaskNames(schedule):
    userInput = string.whitespace
    print('Now, let\'s name our tasks...')
    tasks = []
    tasksNb = schedule.taskNb
    while len(tasks) < tasksNb and StringUtils.IsInputValid(userInput):
        print('Please type the name of task #', len(tasks) + 1)
        userInput = input()
        tasks.append(userInput)
    schedule.tasks = tasks