import random
import datetime


# define the class_____________________________________________________________
class KitchenDutyPlanner(object):
    
    def __init__(self):
        self.date = datetime.datetime(2017, 4, 1)
        self.end_date = datetime.datetime(2017, 5, 1)
        self.day = datetime.timedelta(days=1)
        self.online_marketing_team =  [
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
        self.team = None
        self.cleaning_score = {member: 0 for member in self.online_marketing_team}
    
    # make the plan
    def make_plan(self):
        while self.date < self.end_date:
            
            # check if cleaning is needed
            cleaning_needed = self.is_cleaning_needed()
            
            # if cleaning is needed assign two persons
            if cleaning_needed:
                random_persons = self.assign_persons()
                
                # we keep count of who was assigned cleaning duty
                for person in random_persons:
                    self.cleaning_score[person] += 1
            else:
                # set random persons to nothing if cleaning not needed
                random_persons = ""

            # display date and decision and responsible persons
            print(self.date, cleaning_needed, random_persons)

            self.date = self.date + self.day
    
    # check if cleaning is needed for the current date
    def is_cleaning_needed(self):

        # isoweekday: 1 is Monday, 6 is Saturday and 7 is Sunday
        if self.date.isoweekday() in (6, 7):
            return False

        # 14th of April is Good Friday
        if self.date == datetime.datetime(2017, 4, 14):
            return False

        # 17th of April is Easter Monday
        if self.date == datetime.datetime(2017, 4, 17):
            return False

        return True
    
    # get two different random persons
    def assign_persons(self):
        random_person_one = self.get_random_person()

        # loop until we have two different people for kitchen duty
        # can happen if list was empty and a new copy was made
        while True:
            random_person_two = self.get_random_person()
            if random_person_one == random_person_two:
                self.team.append(random_person_two)
            else:
                return (random_person_one, random_person_two)


    # get a random person from self.team
    def get_random_person(self):
        # make sure self.team is not empty
        if not self.team:
            self.team = self.online_marketing_team.copy()
        random.shuffle(self.team)
        
        random_person = self.team.pop()
        
        return random_person


# the main program_____________________________________________________________
planner = KitchenDutyPlanner()  # create an instance of KitchenDutyPlanner
planner.make_plan()
print(planner.cleaning_score)
