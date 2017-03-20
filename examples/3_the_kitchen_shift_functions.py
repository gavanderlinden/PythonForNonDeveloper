import random
import datetime

# static variables_____________________________________________________________
ONLINE_MARKETING_TEAM = [
    "Max Wölfle",
    "Tony van der Linden",
    "Christian Schulz",
    "Tobias Esser",
    "Fabian Reißmüller",
    "Yvonne Kohnle",
    "Johannes Burkhardt",
    "Nicolas Mutter",
    "Martin Kase",
    "Sascia Burri",
    "Patricia Tchorzewski"
]
START_DATE = datetime.datetime(2017, 4, 1)
END_DATE = datetime.datetime(2017, 5, 1)
DAY = datetime.timedelta(days=1)

# functions____________________________________________________________________

# check if cleaning needs to be done
def is_cleaning_needed(date):

    # isoweekday: 1 is Monday, 6 is Saturday and 7 is Sunday
    if date.isoweekday() in (6, 7):
        return False
    
    # 14th of April is Good Friday
    if date == datetime.datetime(2017, 4, 14):
        return False

    # 17th of April is Easter Monday
    if date == datetime.datetime(2017, 4, 17):
        return False
    
    return True


# get two different random team members to do cleaning
def assign_persons(team):

    # we will loop until we get two different people
    team, random_person_one = random_person(team)
    while True:
        team, random_person_two = random_person(team)
        if random_person_one == random_person_two:
            team.append(random_person_two)
        else:
            return team, (random_person_one, random_person_two)


# get a random team member
def random_person(team):
    # make sure team is not empty
    if not team:
        team = ONLINE_MARKETING_TEAM.copy()

    random.shuffle(team)

    random_person = team.pop()

    return team, random_person


# the main program_____________________________________________________________
date = START_DATE
team = None
cleaning_score = {member: 0 for member in ONLINE_MARKETING_TEAM}

while date < END_DATE:
    
    # evaluate if we need to clean
    cleaning_needed = is_cleaning_needed(date)
    
    # if cleaning is needed, assign two persons
    if cleaning_needed:
        team, random_persons = assign_persons(team)
        for person in random_persons:
            cleaning_score[person] += 1
    else:
        random_persons = ""
    
    # display date and decision and responsible person
    print(date, cleaning_needed, random_persons)

    # we need to add a day to date because else we keep evaluating 
    # the same date indefinitely (infinite loop)
    date = date + DAY

print("Cleaning score:", cleaning_score)

