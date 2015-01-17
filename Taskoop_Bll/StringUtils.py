# -*- coding: utf-8 -*-

import re
import string
import calendar
from calendar import datetime

EMAIL_REGEX = '[^@]+@[^@]+\.[^@]+'

NO_KEY = 'N'

QUIT_KEY = 'Q'

YES_KEY = 'Y'

HOUR_KEY = 'H'

DAY_KEY = 'D'

WEEK_KEY = 'W'

MONTH_KEY = 'M'


def IsInputValid(pInput):

    if(pInput.upper() == QUIT_KEY):
        print("See you soon!")
        quit()
    return len(pInput) > 0


def IsYesNoInputValid(pInput):
    pInputUp = pInput.upper()
    return IsInputValid(pInput) and (pInputUp == NO_KEY or pInputUp == YES_KEY)


def IsEmailInputValid(pInput):
    return IsInputValid and re.match(EMAIL_REGEX, pInput)


def IsDateInputValid(pInput):
    pInputUp = pInput.upper()
    
    valid = True
    
    dateMembers = pInputUp.split('/')
    for member in dateMembers:
        valid = valid and IsInputValid(member)
        valid = valid and member.isdigit()
        if not valid:
            return False
    
    if len(dateMembers) != 3:
        return False
    
    day = dateMembers[0]
    month = dateMembers[1]
    year = dateMembers[2]
    
    if (not IsIntegerInputValid(year, 
                               datetime.MINYEAR, 
                               datetime.MAXYEAR)
        or not  IsIntegerInputValid(month, 1, 12)):
        return False
    
    daysInMonth = calendar.monthrange(int(year), int(month))[1] 
    
    return (IsIntegerInputValid(day, 1, daysInMonth))
            


def IsDateIncrementInputValid(pInput):
    pInputUp = pInput.upper()
    return (IsInputValid(pInput)
            and (pInputUp == HOUR_KEY
                or pInputUp == DAY_KEY
                or pInputUp == WEEK_KEY
                or pInputUp == MONTH_KEY))


def IsHourInputValid(pInput):
    return IsIntegerInputValid(pInput, 0, 23)


def IsDayInputValid(pInput):
    return IsIntegerInputValid(pInput, 1, 31)


def IsWeekInputValid(pInput):
    return IsIntegerInputValid(pInput, 1, 52)


def IsMonthInputValid(pInput):
    return IsIntegerInputValid(pInput, 1, 12)


# Validates that an input is an integer between a maximum and a minimum
# (both inclusive)
def IsIntegerInputValid(pInput, minValue, maxValue):
    if not pInput.isdigit() or not IsInputValid:
        return False
    value = int(pInput)
    return value >= minValue and value <= maxValue