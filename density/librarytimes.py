import datetime
from interval import interval, inf, imath

OPENING_TIME_WEEKDAY = {
    'Architectural and Fine Arts Library 1': interval([900, 2300]),
    'Architectural and Fine Arts Library 2': interval([900, 2300]),
    'Architectural and Fine Arts Library 3': interval([900, 2300]),
    'Butler Library 2': interval([0,2400]),
    'Butler Library 3': interval([0,2400]),
    'Butler Library 4': interval([0,2400]),
    'Butler Library 301': interval([0,2400]),
    'Butler Library 5': interval([900,2300]),
    'Butler Library 6': interval([900,2300]),
    'Butler Library stk': interval([900,2300]),
    "JJ's Place": interval([1200,2400], [0,1000]),  
    'John Jay Dining Hall': interval([930,2100]),
    'Lehman Library 2': interval([900,1200]),
    'Lehman Library 3': interval([900,1200]),
    'Lerner 1': interval([730, 2400],[0,100]),
    'Lerner 2': interval([730, 2400],[0,100]),
    'Lerner 3': interval([730, 2400],[0,100]),
    'Lerner 4': interval([730, 2400],[0,100]),
    'Lerner 5': interval([730, 2400],[0,100]),
    'Roone Arledge Auditorium': interval([730, 2400],[0,100]),
    'Science and Engineering Library': interval([900,2400],[0,300]), 
    #put the AM opening hours as the second interval so its easier to get the endpoints
    'Starr East Asian Library': interval([900,2300]),
    'Uris/Watson Library': interval([800,2400]), 
    #TODO: Uris has a different Thursday operating hours
}

OPENING_TIME_THURSDAY = {
    'Architectural and Fine Arts Library 1': interval([900, 2300]),
    'Architectural and Fine Arts Library 2': interval([900, 2300]),
    'Architectural and Fine Arts Library 3': interval([900, 2300]),
    'Butler Library 2': interval([0,2400]),
    'Butler Library 3': interval([0,2400]),
    'Butler Library 4': interval([0,2400]),
    'Butler Library 301': interval([0,2400]),
    'Butler Library 5': interval([900,2300]),
    'Butler Library 6': interval([900,2300]),
    'Butler Library stk': interval([900,2300]),
    "JJ's Place": interval([1200,2400],[0,1000]),  
    'John Jay Dining Hall': interval([930,2100]),
    'Lehman Library 2': interval([900,1200]),
    'Lehman Library 3': interval([900,1200]),
    'Lerner 1': interval([730, 2400],[0,300]),
    'Lerner 2': interval([730, 2400],[0,300]),
    'Lerner 3': interval([730, 2400],[0,300]),
    'Lerner 4': interval([730, 2400],[0,300]),
    'Lerner 5': interval([730, 2400],[0,300]),
    'Roone Arledge Auditorium': interval([730, 2400],[0,300]),
    'Science and Engineering Library': interval([900,2400],[0,300]), 
    #put the AM opening hours as the second interval so its easier to get the endpoints
    'Starr East Asian Library': interval([900,2300]),
    'Uris/Watson Library': interval([800,2200]), 
    #TODO: Uris has a different Thursday operating hours
}

OPENING_TIME_FRIDAY = {
	'Architectural and Fine Arts Library 1': interval([900,2100]),
	'Architectural and Fine Arts Library 2': interval([900,2100]),
    'Architectural and Fine Arts Library 3': interval([900,2100]),
    'Butler Library 2': interval([0,2400]),
    'Butler Library 3': interval([0,2400]),
    'Butler Library 4': interval([0,2400]),
    'Butler Library 301': interval([0,2400]),
    'Butler Library 5': interval([900,2100]),
    'Butler Library 6': interval([900,2100]),
    'Butler Library stk': interval([900,2100]),
    "JJ's Place": interval([1200,2400], [0,1000]),
    'John Jay Dining Hall': interval(), 
    #interval() will return "NOT OPEN TODAY", len(interval()) == 0
    'Lehman Library 2': interval([900,1900]),
    'Lehman Library 3': interval([900,1900]),
    'Lerner 1': interval([730, 2400],[0,300]),
    'Lerner 2': interval([730, 2400],[0,300]),
    'Lerner 3': interval([730, 2400],[0,300]),
    'Lerner 4': interval([730, 2400],[0,300]),
    'Lerner 5': interval([730, 2400],[0,300]),
    'Roone Arledge Auditorium': interval([730, 2400],[0,300]),
    'Science and Engineering Library': interval([900,2400],[0,100]),
    'Starr East Asian Library': interval([900,1900]),
    'Uris/Watson Library': interval([800,2100]),
}

OPENING_TIME_SATURDAY = {
	'Architectural and Fine Arts Library 1': interval([1000,2100]),
	'Architectural and Fine Arts Library 2': interval([1000,2100]),
    'Architectural and Fine Arts Library 3': interval([1000,2100]),
    'Butler Library 2': interval([0,2400]),
    'Butler Library 3': interval([0,2400]),
    'Butler Library 4': interval([0,2400]),
    'Butler Library 301': interval([0,2400]),
    'Butler Library 5': [1100,1800],
    'Butler Library 6': [1100,1800],
    'Butler Library stk': [1100,1800],
    "JJ's Place": interval([1200,2400], [0,1000]),
    'John Jay Dining Hall': interval(),
    'Lehman Library 2': [1000,1800],
    'Lehman Library 3': [1000,1800],
    'Lerner 1': interval([800, 2400],[0,300]),
    'Lerner 2': interval([800, 2400],[0,300]),
    'Lerner 3': interval([800, 2400],[0,300]),
    'Lerner 4': interval([800, 2400],[0,300]),
    'Lerner 5': interval([800, 2400],[0,300]),
    'Roone Arledge Auditorium': interval([800, 2400],[0,300]),
    'Science and Engineering Library': interval([1000,2300]),
    'Starr East Asian Library': interval([1200,1900]),
    'Uris/Watson Library': interval([1000,1800]),
}

OPENING_TIME_SUNDAY = {
	'Architectural and Fine Arts Library 1': interval([1200,2200]),
	'Architectural and Fine Arts Library 2': interval([1200,2200]),
    'Architectural and Fine Arts Library 3': interval([1200,2200]),
    'Butler Library 2': interval([0,2400]),
    'Butler Library 3': interval([0,2400]),
    'Butler Library 4': interval([0,2400]),
    'Butler Library 301': interval([0,2400]),
    'Butler Library 5': [1200,2300],
    'Butler Library 6': [1200,2300],
    'Butler Library stk': [1200,2300],
    "JJ's Place": interval([1200,2400], [0,1000]),
    'John Jay Dining Hall': interval([930,2100]),
    'Lehman Library 2': interval([1100,2300]),
    'Lehman Library 3': interval([1100,2300]),
    'Lerner 1': interval([800, 2400],[0,100]),
    'Lerner 2': interval([800, 2400],[0,100]),
    'Lerner 3': interval([800, 2400],[0,100]),
    'Lerner 4': interval([800, 2400],[0,100]),
    'Lerner 5': interval([800, 2400],[0,100]),
    'Roone Arledge Auditorium': interval([800, 2400],[0,100]),
    'Science and Engineering Library': interval([1100,2400],[0,300]),
    'Starr East Asian Library': interval([1200,2200]),
    'Uris/Watson Library': interval([1000,2300]),
}

OPENING_TIME = [OPENING_TIME_WEEKDAY,
                OPENING_TIME_WEEKDAY,
                OPENING_TIME_WEEKDAY,
                OPENING_TIME_THURSDAY,
                OPENING_TIME_FRIDAY,
                OPENING_TIME_SATURDAY,
                OPENING_TIME_SUNDAY,]


def dict_for_time():
    # get library opening times according to today's day in a week
    today = datetime.datetime.today()
    weekday = today.weekday()
    library_times = OPENING_TIME[weekday - 1]

    # get the current hour and minute in the format HHMM
    current_time = datetime.datetime.now().hour * 100 + datetime.datetime.now().minute
    
    message = {}

    for group_name in library_times.keys():
        print (group_name)
        print(library_times[group_name])
        message[group_name] = get_opening_and_closing_time(current_time, library_times[group_name])

    return message


def get_opening_and_closing_time(current_time, interval):
    # get closing time
    if (current_time in interval):
        close_hour = int (interval[0].sup / 100)
        #if the library's closing hour goes beyond midnight
        if (close_hour < 12): 
            output = " Closes at " + str(close_hour) + "AM"
        #if the library closes before midnight
        else:
            
            output = " Closes at " + str(close_hour - 12) + "PM"

    # get opening time 
    else:
        if (len(interval) == 2):
            open_hour = int (interval[1].sup / 100)
        else:
            open_hour = int (interval[0].sup / 100)

        output = " Opens at " + str(open_hour) + "AM"

    return output
      


