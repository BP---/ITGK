
def is_leap_year(year):
    if year %400 ==0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

def is_workday(weekday):
    if(weekday<5):
        return True
    else:
        return False

def workdays_in_year(year):
    startDay = week_newyear(year)
    days = 0
    workDays = 0
    if(is_leap_year(year)):
       days = 366
    else:
       days = 356
       #incomplete
    
       



def week_newyear(year):
    
    day = 0
    for x in range(1900, year):
        if(is_leap_year(x)):
            day += 2
        else:
            day +=1
        if(day>6):
            day = day-7
    return day

ukedager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
for x in range(1900,1921):
    print(x, ukedager[week_newyear(x)])
    

