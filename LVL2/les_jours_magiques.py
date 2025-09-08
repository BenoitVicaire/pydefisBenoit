from datetime import date, timedelta, datetime

jour_magique_count=0
dico_trad={"Monday":"Lundi","Tuesday":"Mardi","Wednesday":"Mercredi","Thursday":"Jeudi","Friday":"Vendredi","Saturday":"Samedie","Sunday":"Dimanche"}

# d=datetime.date(2008,3,4)
# print(d.strftime("%A"))


def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

start_date = date(2000, 1, 1)
end_date = date(2025, 9, 8)
for single_date in daterange(start_date, end_date):
    # print(single_date.strftime("%Y-%m-%d"))
    day_name=single_date.strftime("%A")
    trad_day=dico_trad[day_name]
    if((len(trad_day)+int(single_date.strftime("%d")))%10==0):
        jour_magique_count+=1
print(jour_magique_count)